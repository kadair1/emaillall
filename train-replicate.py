import replicate

training = replicate.trainings.create(
  version="meta/llama-2-7b:bf0a2a692f015ee21527ed2668e338032c1f937b4fcfa1f217f5cd79bf33478c",
  input={
    "train_data": "https://replicate.delivery/pbxt/JXbL95MfBlMb4EjkVGAirAh7XnHMdLy8mEI8I5LtMZh8Fug8/data.jsonl",
    "num_train_epochs": 3
  },
  destination="elizabethsiegle/agihouse-sf-rip"
)

print(training)