MODEL_SAVE_PATH:=volumes/models
LANGUAGE_MODEL_NAME:=all-MiniLM-L6-v2-Q4_K_M-v2.gguf
LANGUAGE_MODEL_URL:=https://huggingface.co/aisuko/all-MiniLM-L6-v2-gguf/resolve/main/all-MiniLM-L6-v2-Q4_K_M-v2.gguf?download=true

.PHONY: download
download:
	@mkdir -p $(MODEL_SAVE_PATH) && [ -f $(MODEL_SAVE_PATH)/$(LANGUAGE_MODEL_NAME) ] || wget -O $(MODEL_SAVE_PATH)/$(LANGUAGE_MODEL_NAME) $(LANGUAGE_MODEL_URL)


.PHONY: up
up:
	@docker compose -f docker-compose.yaml up -d