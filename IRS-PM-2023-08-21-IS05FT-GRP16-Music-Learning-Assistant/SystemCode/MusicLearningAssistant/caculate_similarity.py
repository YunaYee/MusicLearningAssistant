import librosa
import numpy as np
import openl3
import soundfile as sf
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Define function to extract Mel spectrum features
def extract_mel_spectrogram(audio_file):
     # Read audio files
     y, sr = librosa.load(audio_file, sr=None)

     # Extract Mel spectrum features
     mel_spectrogram = librosa.feature.melspectrogram(y, sr=sr)

     return mel_spectrogram

# Define function to calculate cosine similarity
def cosine_similarity(feature1, feature2):
     # Flatten features into one-dimensional vectors
     flat_feature1 = feature1.flatten()
     flat_feature2 = feature2.flatten()

     # Calculate cosine similarity
     dot_product = np.dot(flat_feature1, flat_feature2)
     norm_feature1 = np.linalg.norm(flat_feature1)
     norm_feature2 = np.linalg.norm(flat_feature2)
     similarity = dot_product / (norm_feature1 * norm_feature2)

     return similarity

# Paths to two audio files
audio_file1 = 'audio1.wav'
audio_file2 = 'audio2.wav'

#Extract audio features
audio1, sr1 = sf.read(audio_file1)
audio2, sr2 = sf.read(audio_file2)

#Extract audio features (OpenL3 uses the latest audio feature model by default)
features1, timestamps1 = openl3.get_audio_embedding(audio1, sr1)
features2, timestamps2 = openl3.get_audio_embedding(audio2, sr2)

# Calculate audio similarity (cosine similarity)
similarity = cosine_similarity(features1, features2)
print("Audio similarity:", similarity[0, 0])

# Extract Mel spectrum features
mel_spectrogram1 = extract_mel_spectrogram(audio_file1)
mel_spectrogram2 = extract_mel_spectrogram(audio_file2)

# Calculate cosine similarity
similarity = cosine_similarity(mel_spectrogram1, mel_spectrogram2)

print(f"Cosine Similarity between {audio_file1} and {audio_file2}: {similarity}")