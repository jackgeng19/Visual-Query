# Visual-Query

##
Query an visual object. 
{"key": "visual_object", "value": "timestamp_last_appear"}

## QA Data Automation

### Current chat-gpt prompt description
Identify objects appear in the text and ask the question where that object appear in the video.

### Problem with current policy
- The json file contains annotation and summary. The summaries largely contains physical object, but the annotations contains mostly movements that are not descriptive e.g. X moves his head around. And the non-descriptive annotation will make gpt ask questions that does not make sense. Do we ignore annotations to avoid noise in the data?
- The current policy will identify each object and a timestamp when they show up in the text. For example, if in two separate time intervals of one clip, a yellow key appears in both time intervals, then the data will contain two different timestamp for that single object. However, we want to identify the time when the object last appears. Should we use another policy that takes all the texts in one video clip and ask gpt the question of "when does that object last appears?" 
  - Pros of the other design:
    - The data will only have timestamp for the last occurance of an object.
  - Cons of the other design:
    - Hard to verify the correctness of the data.
    - Hard for the gpt model to output the correct answer given the entire video narration as context: 1. Identify objects that appears. 2. Finding the last occurance of an object.
    
Question: Does containing all timestamps for the occurance of an object affect the legitimacy of the data? If the data gives our model the ability to capture the occurance of an object instead of only capturing the last occurance, does that affect the models ability for visual query? We can train two models using different data for comparison.
