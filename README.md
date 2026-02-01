# 🔍 AI SEO Priority Analysis Tool

A professional web UI for an AI-powered SEO priority analysis agent that helps users identify what to fix first to improve search rankings.

## 🌟 Features

- **Clean & Minimal UI**: Centered layout with intuitive form inputs
- **Smart Priority Analysis**: AI-driven logic to identify critical SEO issues
- **Actionable Recommendations**: Get specific actions to improve your rankings
- **Easy to Use**: Simple form-based interface requiring no technical expertise

## 🎯 Priority Analysis Logic

The tool analyzes your page based on multiple factors and provides prioritized recommendations:

1. **Technical SEO** (Highest Priority) - If page is not indexed OR PageSpeed score < 50
2. **Content Priority** - If content length < 800 words
3. **On-Page SEO** - If missing title tag or meta description
4. **Off-Page SEO** - If all above are satisfied, focus on building authority

## 📋 Input Parameters

- **Website URL**: The page you want to analyze
- **Indexed**: Whether the page appears in search results
- **Content Length**: Word count of the page content
- **Title Tag**: Presence of title tag
- **Meta Description**: Presence of meta description
- **PageSpeed Score**: Google PageSpeed Insights score (0-100)

## 🚀 Running Locally

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/listandsouzaq/seo-ai-agent-ui.git
cd seo-ai-agent-ui
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## ☁️ Deploying to Streamlit Cloud

1. Fork this repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with your GitHub account
4. Click "New app"
5. Select this repository and set:
   - **Main file path**: `app.py`
   - **Python version**: 3.9 or higher
6. Click "Deploy"

Your app will be live at: `https://[your-app-name].streamlit.app`

## 📸 Screenshots

The app features:
- A centered, clean form layout
- Color-coded priority results (Red for Technical, Teal for Content, Yellow for On-page, Purple for Off-page)
- Detailed reasoning and actionable steps
- Expandable summary section

## 🛠️ Technical Stack

- **Framework**: Streamlit 1.31.0
- **Language**: Python 3.8+
- **Deployment**: Streamlit Cloud ready

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📧 Contact

For questions or feedback, please open an issue on GitHub.
