# Visual-Query
(the sample output qa data is under folder "QA_data" The code for generating the data is under "QA_automation")

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

Sample qa data:

{
    "videos.cba13243-5ad3-4360-87df-6286867c473a":
    {
        "annotation_qa":
        [
            "Q: When does man X0 appear?\nA: start_time: 0.0420572, end_time: 0.0420572",
            "Q: When do the green vegetables appear?\nA: start_time: 0, end_time: 0.7925471999999999.",
            "Q: When does C appear?\nA: start_time: 11.898337199999999, end_time: 11.898337199999999.\n\nQ: What objects appear in the clip?\nA: Vegetables.\n\nQ: When does the vegetable appear?\nA: start_time: 11.898337199999999, end_time: 11.898337199999999.",
            "Q: When does the vegetable drop on the chair?\nA: start_time: 13.072057199999998, end_time: 13.072057199999998.",
            "Q: When does the separator appear?\nA: start_time: 13.831647199999999, end_time: 13.831647199999999.",
            "Q: When does the vegetable being picked appear?\nA: start_time: 14.5081572, end_time: 14.5081572.",
            "Q: When does C start cutting the vegetable?\nA: start_time: 15.2878172, end_time: (not provided)\n\nQ: Is there any physical object used to cut the vegetable?\nA: (not mentioned in the description)\n\nQ: Any other physical object present in the video?\nA: (not mentioned in the description) - no objects.",
            "Q: When does the vegetable drop appear?\nA: start_time: 17.110057200000004, end_time: 17.110057200000004. \n\nQ: Are there any other physical objects in the video?\nA: No objects.",
            "Q: When does C pick a vegetable?\nA: start_time: 18.425877200000002, end_time: 18.425877200000002.",
            "Q: When does the vegetable appear being cut by #C with her hands?\nA: start_time: 19.617977200000002 , end_time: 19.617977200000002 .",
            "Q: When does the vegetable appear on the chair?\nA: start_time: 22.831057200000004, end_time: 22.831057200000004.",
            "Q: When does dirt appear on the floor?\nA: start_time: 23.555637200000003, end_time: 23.555637200000003.",
            "Q: When does C pick a vegetable?\nA: start_time: 24.096737200000003, end_time: 24.096737200000003.",
            "Q: When does the vegetable appear?\nA: start_time: 25.988077200000003, end_time: 25.988077200000003.",
            "Q: When does the vegetable appear?\nA: start_time: 28.2100572, end_time: 28.2100572.",
            "Q: When does the dirt appear?\nA: start_time: 28.885057200000002, end_time: 28.885057200000002.",
            "Q: When does C pick a vegetable from the bunch of vegetables?\nA: start_time: 29.0375872, end_time: 29.0375872.",
            "Q: When does the vegetable appear?\nA: start_time: 29.929777200000004, end_time: 29.929777200000004.",
            "Q: When does the vegetable appear?\nA: start_time: 31.5598972, end_time: 31.5598972.",
            "Q: When does C pick a vegetable from the bunch of vegetables? \nA: start_time: 32.092317200000004, end_time: 32.092317200000004."
        ],
        "summary_qa":
        [
            "Q: When does the naan appear?\nA: start_time: 3240.021028645833, end_time: 3540.021028645833.",
            "Q: When does the rolling pin appear?\nA: start_time: 3240.021028645833, end_time: 3330.021028645833.\n\nQ: When does the skimmer appear?\nA: start_time: 3390.021028645833, end_time: 3540.021028645833.\n\nQ: Any other physical objects?\nA: No objects.",
            "Q: When does the firewood appear?\nA: start_time: 2700.021028645833, end_time: 2710.021028645833.\n\nQ: When does the dough appear?\nA: start_time: 2710.021028645833, end_time: 2750.021028645833.\n\nQ: When does the rolling pan appear?\nA: start_time: 2750.021028645833, end_time: 2800.021028645833.\n\nQ: Are there any other physical objects present in the video?\nA: No objects.",
            "Q: When does the dough appear?\nA: start_time: 2970.021028645833, end_time: 3270.021028645833.\nQ: When does the roti appear?\nA: start_time: 2970.021028645833, end_time: 3270.021028645833.\nQ: any other physical objects?\nA: no objects.",
            "Q: When does the fire appear?\nA: start_time: 2430.021028645833, end_time: 2440.021028645833.\n\nQ: When does the water pump appear?\nA: start_time: 2435.021028645833, end_time: 2445.021028645833.\n\nQ: When do the cereals appear?\nA: start_time: 2720.021028645833, end_time: 2730.021028645833. \n\nQ: Are there any other physical objects in the description?\nA: No objects.",
            "Q: When does the rolling pin appear?\nA: start_time: 2970.021028645833, end_time: 2983.3543629791665.\n\nQ: When does the oil appear?\nA: start_time: 2983.3543629791665, end_time: 2996.6876963125.\n\nQ: When does person P0 appear?\nA: start_time: 2996.6876963125, end_time: 3270.021028645833.",
            "Q: When does the tray appear?\nA: start_time: 2700.021028645833, end_time: 2710.021028645833.\n\nQ: When does the rolling pin appear?\nA: start_time: 2720.021028645833, end_time: 2790.021028645833.\n\nQ: When does the dough appear?\nA: start_time: 2720.021028645833, end_time: 2790.021028645833.\n\nQ: When does the kitchen appear?\nA: start_time: 2700.021028645833, end_time: 3000.021028645833.",
            "Q: When does the rolling pin appear?\nA: start_time: 3260.021028645833, end_time: 3280.021028645833.\n\nQ: When does the draining spoon appear?\nA: start_time: 3300.021028645833, end_time: 3320.021028645833.\n\nQ: When does the saucepan appear?\nA: start_time: 3340.021028645833, end_time: 3400.021028645833.\n\nQ: When does the frying pan appear?\nA: start_time: 3400.021028645833, end_time: 3460.021028645833.\n\nQ: When does the African donut appear?\nA: start_time: 3240.021028645833, end_time: 3300.021028645833.\n\nQ: When does the woman P appear?\nA: start_time: 3240.021028645833, end_time: 3540.021028645833.\n\nno objects",
            "Q: When does the fire appear?\nA: start_time: 2430.021028645833, end_time: 2730.021028645833.\n\nQ: When does the cow dung charcoal appear?\nA: start_time: 2430.021028645833, end_time: 2730.021028645833.\n\nQ: When does the cooking pot appear?\nA: start_time: 2430.021028645833, end_time: 2730.021028645833.\n\nQ: When does the tray appear?\nA: start_time: 2430.021028645833, end_time: 2730.021028645833.",
            "Q: When does C appear?\nA: start_time: 5293.287695266667, end_time: 5316.487695266666.\n\nQ: When does man X appear?\nA: start_time: Unknown, end_time: Unknown.\n\nQ: When does Boy Y appear?\nA: start_time: Unknown, end_time: Unknown.\n\nQ: When does the yard appear?\nA: start_time: Unknown, end_time: Unknown.\n\nQ: When does any physical object appear?\nA: no objects.",
            "Q: When does the cow dung appear?\nA: start_time: 5293.287695266667, end_time: 5293.787695266667.",
            "Q: When does the stove appear?\nA: start_time: 5295.787695266666, end_time: 5316.487695266666.\n\nQ: When does the cooking happen?\nA: start_time: 5293.287695266667, end_time: 5316.487695266666.\n\nQ: When does the charcoal appear?\nA: start_time: 5296.787695266666, end_time: 5316.487695266666.\n\nQ: When does the man appear?\nA: start_time: 5293.287695266667, end_time: 5316.487695266666.",
            "Q: When does the cooking stones appear?\nA: start_time: 5293.287695266667, end_time: 5296.287695266667.\n\nQ: When does the fire appear?\nA: start_time: 5296.287695266667, end_time: 5300.987695266667.\n\nQ: When does the pullover appear?\nA: start_time: 5303.487695266667, end_time: 5306.487695266667.\n\nQ: When does C appear?\nA: start_time: 5293.287695266667, end_time: 5316.487695266666.\n\nQ: When does anything else physical appear?\nA: no objects.",
            "Q: When does the wood appear?\nA: start_time: 5293.287695266667, end_time: 5316.487695266666.",
            "Q: When does the dung fuel appear?\nA: start_time: 5293.287695266667, end_time: 5316.487695266666.",
            "Q: When does the firewood appear?\nA: start_time: 5293.287695266667, end_time: 5316.487695266666.",
            "Q: When does the cow dung appear?\nA: start_time: 5293.287695266667, end_time: 5297.027695266666.\n\nQ: When does the traditional mud stove appear?\nA: start_time: 5299.067695266666, end_time: 5302.467695266666.\n\nQ: When does man X0 appear?\nA: start_time: 5313.447695266666, end_time: 5316.487695266666.",
            "Q: When does the fire appear?\nA: start_time: 5293.287695266667, end_time: 5316.487695266666.\n\nQ: When does C appear?\nA: start_time: 5293.287695266667, end_time: 5316.487695266666.\n\nQ: When does the key appear?\nA: no objects. \n\nQ: When does the spoon appear?\nA: no objects.\n\nQ: When does the phone appear?\nA: no objects.",
            "Q: When does the charcoal appear?\nA: start_time: 5293.287695266667, end_time: 5316.487695266666.\n\nQ: Are there any other physical objects mentioned?\nA: No objects.",
            "Q: When does the cow dung appear?\nA: start_time: 5293.287695266667, end_time: 5294.657695266667.\n\nQ: Are there any other physical objects mentioned in the video clip?\nA: No objects."
        ]
    }
}
