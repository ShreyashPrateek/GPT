# 🤖 Custom GPT - LangChain + Hugging Face

A powerful GPT application built with LangChain and Hugging Face, featuring a beautiful Streamlit interface.

## ✨ Features

- 🧠 **LangChain Integration** - Modern AI framework
- 🤗 **Hugging Face Models** - Access to powerful LLMs
- 💬 **Chat Interface** - Beautiful Streamlit UI
- 🧠 **Memory Management** - Conversation history
- 🔧 **Easy Deployment** - Ready for cloud hosting

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShreyashPrateek/GPT.git
   cd my_gpt_project
   ```

2. **Set up environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure API keys**
   ```bash
   cp .env.example .env
   # Edit .env and add your Hugging Face API token
   ```

4. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

### 🌐 Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set environment variables in Streamlit Cloud settings
5. Deploy!

## 🔑 Environment Variables

- `HUGGINGFACEHUB_API_TOKEN` - Your Hugging Face API token

## 📁 Project Structure

```
my_gpt_project/
├── app/                 # Core application logic
├── ui/                  # Streamlit interface
├── templates/           # HTML templates
├── streamlit_app.py     # Main entry point
└── requirements.txt     # Dependencies
```

## 🛠️ Built With

- [LangChain](https://langchain.com/) - AI framework
- [Hugging Face](https://huggingface.co/) - AI models
- [Streamlit](https://streamlit.io/) - Web interface

---

Made with ❤️ by Shreyash Prateek