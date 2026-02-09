# digital-advisory-os
# Initialize the local repository
git init digital-advisory-os
cd digital-advisory-os

# Add a remote pointing to your GitHub repository
git remote add origin https://github.com/acuityconsultingke-hub/digital-advisory-os.git

# Create an initial commit
echo "# Digital Advisory OS" > README.md
git add README.md
git commit -m "Initial commit"

# Push to GitHub (make sure the repository exists on GitHub first)
git branch -M main
git push -u origin main
