# 🚀 Explify Deployment Guide for Streamlit Cloud

## 📋 Prerequisites

Before deploying to Streamlit Cloud, ensure you have:
- ✅ A GitHub account
- ✅ A Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- ✅ Your Explify project files

---

## 🎯 Deployment Steps

### Step 1: Prepare Your GitHub Repository

#### Option A: Create a New Repository

1. **Go to GitHub** and create a new repository:
   - Repository name: `explify` (or any name you prefer)
   - Description: "Multimodal AI Explainer with Gemini 1.5 Flash"
   - Visibility: Public (required for free Streamlit Cloud tier)
   - ✅ Initialize with README (optional)

2. **Clone the repository locally**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/explify.git
   cd explify
   ```

3. **Add your Explify files**:
   - Copy `explify_app.py`, `requirements.txt`, and `README.md` to the repository folder
   - Do NOT add `.env` file (we'll use Streamlit Secrets instead)

4. **Create a `.gitignore` file**:
   ```bash
   echo -e ".env\nexplify_env/\n__pycache__/\n*.pyc\n.DS_Store" > .gitignore
   ```

5. **Commit and push**:
   ```bash
   git add .
   git commit -m "Initial commit: Explify app"
   git push origin main
   ```

#### Option B: Use Existing Repository

Simply add the Explify files to your existing repository and push:
```bash
git add explify_app.py requirements.txt README.md
git commit -m "Add Explify app"
git push
```

---

### Step 2: Deploy to Streamlit Cloud

1. **Go to [Streamlit Cloud](https://share.streamlit.io/)**

2. **Sign in with GitHub**
   - Authorize Streamlit to access your repositories

3. **Click "New app"** (top right)

4. **Configure deployment**:
   ```
   Repository:     YOUR_USERNAME/explify
   Branch:         main (or master)
   Main file path: explify_app.py
   App URL:        explify (customize your subdomain)
   ```

5. **Click "Deploy"** 
   - Initial deployment takes 2-3 minutes
   - You'll see build logs in real-time

---

### Step 3: Configure Secrets (API Key)

**IMPORTANT**: Never commit API keys to GitHub!

1. **While your app is deploying**, click the **"⚙️ Settings"** button (top right)

2. **Navigate to "Secrets"** section

3. **Add your Gemini API key**:
   ```toml
   GEMINI_API_KEY = "your_actual_gemini_api_key_here"
   ```
   
   ⚠️ **Format matters**: Use the exact format above (TOML syntax)

4. **Click "Save"**

5. **Your app will automatically restart** with the new secret

---

### Step 4: Verify Deployment

1. **Open your app URL**: `https://YOUR_APP_NAME.streamlit.app`

2. **Check functionality**:
   - ✅ API key is auto-loaded (green checkmark in sidebar)
   - ✅ Test text summarization
   - ✅ Upload and test an image
   - ✅ Upload and test a video (may take 1-2 minutes)

3. **Monitor logs**: Click "Manage app" → "Logs" to see real-time activity

---

## 🔧 Advanced Configuration

### Custom Domain (Optional)

1. Go to **App Settings** → **General**
2. Add your custom domain under "Custom subdomain"
3. Update DNS settings with your domain provider:
   ```
   CNAME record: your-domain.com → YOUR_APP.streamlit.app
   ```

### Resource Limits

**Free Tier Limits**:
- **CPU**: 1 core (shared)
- **RAM**: 1 GB
- **Storage**: Ephemeral (resets on sleep)
- **Sleep time**: After 7 days of inactivity

**Tips for optimization**:
- Videos: Recommend max 50MB uploads
- Use `.stcache_resource` for model initialization if needed
- Monitor resource usage in logs

### Environment Variables (Optional)

Add more secrets in the Secrets section:
```toml
GEMINI_API_KEY = "your_api_key"
MAX_VIDEO_SIZE_MB = "100"
DEFAULT_TEMPERATURE = "0.7"
```

Access in code:
```python
import streamlit as st
max_size = st.secrets.get("MAX_VIDEO_SIZE_MB", "100")
```

---

## 🐛 Troubleshooting

### Issue: "App is not loading"

**Solution**:
1. Check build logs for errors
2. Verify `requirements.txt` has correct package versions
3. Ensure `explify_app.py` has no syntax errors

### Issue: "ModuleNotFoundError"

**Solution**:
```bash
# Make sure requirements.txt includes all dependencies
streamlit==1.31.0
google-generativeai==0.3.2
python-dotenv==1.0.0
Pillow==10.2.0
```

### Issue: "API Key not working"

**Solution**:
1. Go to Settings → Secrets
2. Verify format: `GEMINI_API_KEY = "key_here"`
3. Check for extra spaces or quotes
4. Restart app: Settings → "Reboot app"

### Issue: "Video processing timeout"

**Solution**:
- Video processing may take 1-2 minutes
- For large videos (>100MB), consider:
  ```python
  # Add file size check
  if uploaded_video.size > 100 * 1024 * 1024:  # 100MB
      st.warning("Large video detected. Processing may take several minutes.")
  ```

### Issue: "App keeps sleeping"

**Solution**:
- Free tier apps sleep after 7 days of inactivity
- Upgrade to paid tier for always-on hosting
- Or use a service like UptimeRobot to ping your app every 5 minutes

---

## 📊 Monitoring & Analytics

### View App Analytics

1. Go to [Streamlit Cloud Dashboard](https://share.streamlit.io/)
2. Select your app
3. View:
   - **Viewer count**: Number of active users
   - **Resource usage**: CPU/RAM consumption
   - **Logs**: Real-time application logs
   - **Errors**: Stack traces and exceptions

### Enable Google Analytics (Optional)

Add to `explify_app.py` (before any st.commands):
```python
# Add Google Analytics tracking
st.markdown("""
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
""", unsafe_allow_html=True)
```

---

## 🔄 Updating Your App

### Method 1: Git Push (Automatic)

```bash
# Make changes to your code
git add .
git commit -m "Update feature X"
git push origin main
```
✅ **Streamlit Cloud auto-deploys** within 1-2 minutes

### Method 2: Manual Reboot

1. Go to Streamlit Cloud dashboard
2. Select your app
3. Click "⚙️" → "Reboot app"

---

## 💰 Pricing Tiers

### Free Tier
- ✅ Unlimited public apps
- ✅ 1 GB RAM per app
- ✅ Community support
- ⚠️ Apps sleep after 7 days inactivity

### Team Tier ($20/month)
- ✅ Private apps
- ✅ 4 GB RAM per app
- ✅ Priority support
- ✅ No sleep mode

### Enterprise
- ✅ SSO/SAML
- ✅ Custom resources
- ✅ SLA guarantees
- ✅ Dedicated support

[View pricing](https://streamlit.io/cloud)

---

## 🔐 Security Best Practices

### ✅ DO:
- Store API keys in Streamlit Secrets
- Use `.gitignore` to exclude `.env` files
- Enable 2FA on your GitHub account
- Regularly rotate API keys
- Monitor logs for suspicious activity

### ❌ DON'T:
- Commit API keys to GitHub
- Share your app's secret management URL
- Store sensitive data in session state long-term
- Use production API keys for development

---

## 🌐 Sharing Your App

Once deployed, share your app:

### Direct Link
```
https://YOUR_APP_NAME.streamlit.app
```

### Embed in Website
```html
<iframe 
  src="https://YOUR_APP_NAME.streamlit.app/?embedded=true" 
  width="100%" 
  height="800px" 
  frameborder="0">
</iframe>
```

### QR Code
Generate a QR code for mobile access:
- Use [QR Code Generator](https://www.qr-code-generator.com/)
- Enter your app URL
- Download and share

---

## 📈 Performance Optimization

### Caching for Better Performance

Add caching to the model initialization:

```python
@st.cache_resource
def get_model(temperature):
    """Cache model instance"""
    return genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        generation_config={
            'temperature': temperature,
            'top_p': 0.95,
            'top_k': 40,
            'max_output_tokens': 2048,
        }
    )
```

### Optimize File Uploads

```python
# Add file size validation
MAX_FILE_SIZE_MB = 100

if uploaded_video:
    file_size_mb = uploaded_video.size / (1024 * 1024)
    if file_size_mb > MAX_FILE_SIZE_MB:
        st.error(f"❌ File too large: {file_size_mb:.1f}MB. Max: {MAX_FILE_SIZE_MB}MB")
        st.stop()
```

---

## 🎓 Additional Resources

- 📚 [Streamlit Documentation](https://docs.streamlit.io/)
- 🤖 [Gemini API Documentation](https://ai.google.dev/docs)
- 💬 [Streamlit Community Forum](https://discuss.streamlit.io/)
- 🐙 [Example Streamlit Apps](https://streamlit.io/gallery)

---

## ✅ Deployment Checklist

Before going live, verify:

- [ ] All files pushed to GitHub
- [ ] `.gitignore` includes `.env`
- [ ] `requirements.txt` is up to date
- [ ] API key added to Streamlit Secrets
- [ ] App successfully deploys
- [ ] Test all three modes (Text, Image, Video)
- [ ] Error messages are user-friendly
- [ ] Mobile responsiveness checked
- [ ] README.md updated with live app link
- [ ] Monitoring/analytics configured (optional)

---

## 🎉 You're Live!

Congratulations! Your Explify app is now deployed on Streamlit Cloud!

**Next Steps**:
1. Share your app URL with users
2. Gather feedback and iterate
3. Monitor usage and performance
4. Consider upgrading if you need more resources

**Need help?** Join the [Streamlit Discord](https://discord.gg/streamlit) or post on the [forum](https://discuss.streamlit.io/).

---

Made with ⚡ by Explify | Deployed on Streamlit Cloud
