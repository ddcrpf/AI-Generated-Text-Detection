import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def plot_prediction(probability, save_path="static/prediction_plot.png"):
    labels = ['LLM Generated', 'Human Generated']
    probabilities = [1 - probability, probability]
    
    plt.figure(figsize=(6, 4))
    plt.bar(labels, probabilities, color=['blue', 'green'])
    plt.ylim(0, 1)
    plt.ylabel('Probability')
    plt.title('Text Classification Probability')
    
    for i, v in enumerate(probabilities):
        plt.text(i, v + 0.02, f"{v:.2f}", ha='center', fontsize=12)
    
    plt.savefig(save_path)
    plt.close()  # Close the figure to free memory


def generate_wordcloud(text, save_path="static/wordcloud.png"):
    # Generate a word cloud image
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    
    # Plot the word cloud
    plt.figure(figsize=(8, 4))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    
    # Save the word cloud image
    plt.savefig(save_path)
    plt.close() 