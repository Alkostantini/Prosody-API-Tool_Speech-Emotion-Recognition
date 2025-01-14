import os
import numpy as np
import pandas as pd
from funasr import AutoModel


class Emotion2Vec:
    def __init__(self):

        self.model = AutoModel(
            model="iic/emotion2vec_plus_large", device="cuda"
        )  # Alternative: iic/emotion2vec_plus_seed, iic/emotion2vec_plus_base, iic/emotion2vec_plus_large and iic/emotion2vec_base_finetuned

        self.label_mapper = LabelMapper()

    # todo: explore the streaming capabilities of the model
    def predict(self, audio_path, granularity="utterance"):
        rec_result = self.model.generate(
            audio_path, granularity="utterance", extract_embedding=False
        )[0]
        print(rec_result["labels"][np.argmax(rec_result["scores"])])
        print('rec_result:', rec_result)

        # class names
        # ['生气/angry', '厌恶/disgusted', '恐惧/fearful', '开心/happy', '中立/neutral', '其他/other', '难过/sad', '吃惊/surprised', '<unk>']
        predicted_class = self.label_mapper.map_to_system(
            np.argmax(rec_result["scores"])
        )
        predicted_probs = self.label_mapper.reorder_probabilities(rec_result["scores"])

        return predicted_class, predicted_probs


class LabelMapper:
    def __init__(self):
        # todo handle that both other and unkown are mapped to Noise
        self.upstream_to_system_mapping = {
            "生气/angry": "angry",
            "厌恶/disgusted": "disgust",
            "恐惧/fearful": "fear",
            "开心/happy": "happy",
            "中立/neutral": "neutral",
            "其他/other": "Noise",
            "难过/sad": "sad",
            "吃惊/surprised": "surprise",
            "<unk>": "Noise",
        }

        self.upstream_to_system_mapping_int = {
            0: "angry",
            1: "disgust",
            2: "fear",
            3: "happy",
            4: "neutral",
            5: "Noise",
            6: "sad",
            7: "surprise",
            8: "Noise",
        }

        self.system_to_upstream_mapping_int = {
            v: k for k, v in self.upstream_to_system_mapping_int.items()
        }

        self.system_labels = [
            "Noise",
            "angry",
            "disgust",
            "fear",
            "happy",
            "neutral",
            "sad",
            "surprise",
        ]

    def map_to_system(self, upstream_label):
        if type(upstream_label) == str:
            return self.upstream_to_system_mapping.get(upstream_label, None)
        else:
            return self.upstream_to_system_mapping_int.get(upstream_label, None)

    def reorder_probabilities(self, upstream_probabilities):
        # reorder probabilities based on system labels
        reordered_probabilities = [
            upstream_probabilities[self.system_to_upstream_mapping_int.get(label)]
            for label in self.system_labels
        ]
        return np.array(reordered_probabilities)


# if __name__ == "__main__":

#     # wav_file = f"{model.model_path}/example/test.wav"
# #    base_dir = r"/home/deep/Prosody/OwnVoiceData_Emotions"

#     #wav_dir = f"{base_dir}/Wav"
#     wav_dir = r"./Database_Interview"

#     wav_files = sorted([file for file in os.listdir(wav_dir) if file.endswith(".wav")])

#     emotion2vec = Emotion2Vec()

#     for wav_file in wav_files:
#         emotion, probabilities = emotion2vec.predict(os.path.join(wav_dir, wav_file))
#         print(f"Predicted emotion in {wav_file}: {emotion}")
#         print(f"Predicted emotion in {wav_file}: {probabilities}")

