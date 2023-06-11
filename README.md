# Visual-Query
(the sample output qa data is under folder "QA_data" The code for generating the data is under "QA_automation")
View sampe generated QA data without download the json: http://jsonblob.com/1117586296569872384

## Goal: Query an visual object. 
{"key": "visual_object", "value": "timestamp_last_appear"}

## QA Data Automation

### Current chat-gpt prompt description
Identify objects appear in the text and ask the question when that object appear in the video.

input: the annotation/summary of one single clip from the video with description, start time, and end time.

output: Q: When does object X appear? A: start time - end time.

### Problem with current policy
- The json file contains annotation and summary. The summaries largely contains physical object, but the annotations contains mostly movements that are not descriptive e.g. X moves his head around. And the non-descriptive annotation will make gpt ask questions that does not make sense. Do we ignore annotations to avoid noise in the data?
- The current policy will identify each object and a timestamp when they show up in the text. For example, if in two separate time intervals of one clip, a yellow key appears in both time intervals, then the data will contain two different timestamp for that single object. However, we want to identify the time when the object last appears. Should we use another policy that takes the descriptions of all clips in the entire video and ask gpt the question of "when does that object last appears?"

  - Pros for current design:
    - It is easy for gpt model to identify objects from a single text description (compared to given the whole context in a video).
    - The answer has a larger possiblity to be correct because the timestamp for that specific text description is given in the prompt (It is to say that the job of the gpt model is not to find a timestamp, but instead to identify physical object from the description).
  - Cons for current design:
    - The data will contain multiple timestamp for one single object if that object appears more than once (may not be a problem for our purpose?).
    
  - Pros for the other design:
    - The data will only have timestamp for the last occurance of an object.
  - Cons for the other design:
    - Hard to verify the correctness of the data.
    - Hard for the gpt model to output the correct answer given the entire video narration as context: 1. Identify objects that appears. 2. Finding the last occurance of an object.
    
Question: Does containing all timestamps for the occurance of an object affect the legitimacy of the data? If the data gives our model the ability to capture the occurance of an object instead of only capturing the last occurance, does that affect the models ability for visual query? We can train two models using different data for comparison.

