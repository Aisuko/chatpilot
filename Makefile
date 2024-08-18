MODEL_SAVE_PATH:=volumes/models
LANGUAGE_MODEL_NAME:=all-MiniLM-L6-v2-Q4_K_M-v2.gguf
LANGUAGE_MODEL_URL:=https://huggingface.co/aisuko/all-MiniLM-L6-v2-gguf/resolve/main/all-MiniLM-L6-v2-Q4_K_M-v2.gguf?download=true

INFERNCE_MODEL_NAME:=ft-smollm-135M-instruct-on-hf-ultrafeedback-f16.gguf
INFERNCE_MODEL_URL:=https://huggingface.co/aisuko/ft-smollm-135M-instruct-on-hf-ultrafeedback-gguf/resolve/main/ft-smollm-135M-instruct-on-hf-ultrafeedback-f16.gguf?download=true

.PHONY: download
download:
	@mkdir -p $(MODEL_SAVE_PATH) && [ -f $(MODEL_SAVE_PATH)/$(LANGUAGE_MODEL_NAME) ] || wget -O $(MODEL_SAVE_PATH)/$(LANGUAGE_MODEL_NAME) $(LANGUAGE_MODEL_URL)
	@mkdir -p $(MODEL_SAVE_PATH) && [ -f $(MODEL_SAVE_PATH)/$(INFERNCE_MODEL_NAME) ] || wget -O $(MODEL_SAVE_PATH)/$(INFERNCE_MODEL_NAME) $(INFERNCE_MODEL_URL)

.PHONY: up
up:
	@docker compose -f docker-compose.yaml up -d