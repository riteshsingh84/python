# AITranslator

AITranslator is a Python tool for translating resource files (such as .resx, .json, .csv, and .xml) into multiple languages using any LLM AI model like OpenAI GPT-4o, Google Gemini 2.5 Pro,Claude 4 Opus etc. It is designed to help  localize application resources efficiently and maintain a tone consistent with standard product communication—clear, concise, and customer-friendly.

## Features

- Supports translation of .resx, .json, .csv, and .xml resource files.
- Preserves formatting, line breaks, markdown, HTML tags, and placeholders.
- Batch translation to multiple target languages in one run.
- Configurable prompt and application settings via INI files.
- Error logging for failed translations.

## Getting Started

### 1. Install Dependencies

```sh
pip install -r [requirements.txt]
```

### 2. Configure Settings

- Edit appconfig.ini to set your input/output directories and OpenAI API key.

- Edit promptconfig.ini to customize the translation prompt if needed.

### 3. Prepare Input Files
Place your resource files (e.g., .resx, .json, .csv, .xml) in the input/ directory.

### 4. Run the Translator
Use --languages to specify target languages (by name or code, e.g., en,de,fr,it).

### 5. Output
Translated files will be saved in the output/ directory, with language codes appended to file names.

### 6. Customization
**Prompt Template:** Edit promptconfig.ini to change how the translation prompt is constructed.

**Logging:** Errors are logged to the file specified in appconfig.ini.

## Best AI Model APIs for Batch Translation (Web Applications)
| Model/API                | Translation Quality         | Speed           | Cost (per 1M tokens) | Context Window | Strengths                                                                 | Weaknesses                                 |
|--------------------------|-----------------------------|------------------|----------------------|----------------|---------------------------------------------------------------------------|--------------------------------------------|
| OpenAI GPT-4o            | ⭐⭐⭐⭐⭐ (very high)           | ⚡ Fast           | $3.50                | 128k tokens     | Excellent fluency, context retention, supports function calling          | Slightly expensive for large-scale use     |
| Google Gemini 2.5 Pro    | ⭐⭐⭐⭐½                       | ⚡⚡ Very Fast     | $3.44                | 1M tokens       | Fastest output, strong multilingual support, large context               | Slightly less nuanced than GPT-4o          |
| DeepSeek R1 (May 2025)   | ⭐⭐⭐⭐                        | ⚡⚡ Very Fast     | $0.96                | 128k tokens     | Great value, low latency (2.37s), good for bulk translation              | Slightly lower fluency in complex texts    |
| Claude 4 Opus            | ⭐⭐⭐⭐⭐                      | ⚡ Moderate       | $30.00               | 200k tokens     | Very accurate, especially in legal/medical domains                       | Expensive, slower than others              |
| Mistral 7B/8x22B         | ⭐⭐⭐½                        | ⚡⚡ Fast          | $0.40–$1.00          | 32k–65k tokens  | Lightweight, cost-effective                                               | Less consistent in nuanced translation     |
| Meta LLaMA 3 (70B)       | ⭐⭐⭐⭐                        | ⚡ Moderate       | $1.00–$1.50          | 128k tokens     | Open-source, customizable                                                 | Needs fine-tuning for best results         |

**Note:** Please check the price at real time. Purpose is to show comparison among models.

## License
This project is for educational purposes.

Contributions are welcome!

