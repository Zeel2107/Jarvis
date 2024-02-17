import os
import openai
from config import apikey

openai.api_key = "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"

response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "How to write Blog?"
    },
    {
      "role": "assistant",
      "content": "Writing a blog involves several steps to create engaging and informative content for your readers. Here are some tips on how to write a blog effectively:\n\n1. Choose a Topic: Select a topic that you are passionate about and that you believe will be of interest to your target audience.\n\n2. Research: Conduct thorough research on your chosen topic to gather information, statistics, and facts that will support your blog post.\n\n3. Create an Outline: Organize your ideas and information into a clear and structured outline. This will help you stay focused and ensure your blog post flows smoothly.\n\n4. Write a Compelling Introduction: Start your blog post with a catchy introduction that grabs the reader's attention and entices them to continue reading.\n\n5. Use Subheadings: Break up your content into smaller sections by using subheadings. This makes it easier for readers to scan the post and find the information they are looking for.\n\n6. Write in a Conversational Tone: Keep your writing style conversational and engaging to connect with your readers on a personal level.\n\n7. Provide Value: Offer valuable insights, tips, and information that will benefit your audience and keep them coming back for more.\n\n8. Include Visuals: Use images, infographics, and videos to enhance your blog post and"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''
ChatCompletion(id='chatcmpl-8tAOTrqKurTKRkuFaT9Z9GV1mWMaO', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content=' make it visually appealing to your readers.\n\n9. Proofread and Edit: Before publishing your blog post, be sure to carefully proofread and edit your content for any grammatical errors or typos.\n\n10. Promote Your Blog: Share your blog post on social media, email newsletters, and other platforms to reach a wider audience and drive traffic to your blog.\n\nBy following these steps, you can create high-quality and engaging blog posts that will attract and retain readers. Remember to be consistent in your blogging efforts and always strive to provide valuable content to your audience.', role='assistant', function_call=None, tool_calls=None))], created=1708158685, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint='fp_69829325d0', usage=CompletionUsage(completion_tokens=113, prompt_tokens=272, total_tokens=385))
'''