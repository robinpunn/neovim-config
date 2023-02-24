import { Configuration, OpenAIApi } from "openai";

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

export default async function (req:any, res:any) {
  const completion = await openai.createCompletion({
    model: "text-davinci-002",
    prompt: generatePrompt(req.body.topic),
    temperature: 0.6,
    max_tokens: 1600,
  });
  console.log(completion.data.choices[0].text);
  res.status(200).json({ result: completion.data.choices[0].text });
}

function generatePrompt(topic:string) {
  return `Create an outline for a blog based on the topic of ${topic}.

  1. ${topic} Introduction
  a. Hook: What is the first sentence or paragraph that will grab the reader's attention?
  b. Thesis statement: What is the main argument or point of the post?
2. Body
  a. What are some subtopics related to ${topic}?
     i. Supporting detail: What evidence or examples can be used to support this subtopic?
     ii. Supporting detail: What evidence or examples can be used to support this subtopic?
  b. What are some other subtopics related to ${topic}?
     i. Supporting detail: What evidence or examples can be used to support this subtopic?
     ii. Supporting detail: What evidence or examples can be used to support this subtopic?
  c. What are some additional subtopics related to ${topic}?
     i. Supporting detail: What evidence or examples can be used to support this subtopic?
     ii. Supporting detail: What evidence or examples can be used to support this subtopic?
3. Conclusion
  a. Restate thesis: How can the thesis statement be summarized?
  b. Summarize main points: What are the key takeaways from the post?
  c. Call to action: What action or next steps can readers take related to ${topic}?

`;
}