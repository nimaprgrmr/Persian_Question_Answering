import torch
from transformers import AutoTokenizer, XLMRobertaForQuestionAnswering

device = 'cuda' if torch.cuda.is_available() else 'cpu'
# Initialize the tokenizer and XLM-RoBERTa model
model_name = "pedramyazdipoor/persian_xlm_roberta_large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = XLMRobertaForQuestionAnswering.from_pretrained(model_name)

device = 'cuda' if torch.cuda.is_available() else 'cpu'

context = ''' 
ماده ۱- مصوبات مجلس شورای اسلامی و نتیجه همه‌پرسی پس از طی مراحل قانونی به رئیس‌جمهور ابلاغ می‌شود. رئیس‌جمهور باید ظرف مدت پنج روز آن را امضا و به مجریان ابلاغ نماید و دستور انتشار آن را صادر کند و روزنامه رسمی موظف است ظرف مدت ۷۲ ساعت پس از ابلاغ منتشر نماید.
تبصره – در صورت استنکاف رئیس جمهور از امضا یا ابلاغ در مدت مذکور در این ماده به دستور رئیس مجلس شورای اسلامی روزنامه رسمی موظف است ظرف مدت ۷۲ ساعت مصوبه را چاپ و منتشر نماید
ماده ۲ – قوانین پانزده روز پس از انتشار در سراسر کشور لازم‌الاجرا است مگر آنکه در خود قانون ترتیب خاصی برای موقع اجرا مقرر شده باشد.
ماده ۳ – انتشار قوانین باید در روزنامه رسمی بعمل آید.
ماده ۴ – اثر قانون نسبت بآتیه است و قانون نسبت بماقبل خود اثر ندارد مگر اینکه در خود قانون مقررات خاصی نسبت باین موضوع اتخاذ‌شده باشد.
ماده ۵ – کلیه سکنه ایران اعم از اتباع داخله و خارجه مطیع قوانین ایران خواهند بود مگر درمواردیکه قانون استثناء کرده باشد.
ماده ۶ – قوانین مربوطه باحوال شخصیه از قبیل نکاح و طلاق و اهلیت اشخاص وارث در مورد کلیه اتباع ایران ولو اینکه مقیم در خارجه باشند مجری خواهد بود.
ماده ۷ – اتباع خارجه مقیم در خاک ایران از حیث مسائل مربوطه باحوال شخصیه و اهلیت خود و همچنین از حیث حقوق ارثیه در حدود معاهدات مطیع قوانین و مقررات دولت متبوع خود خواهند بود.
ماده ۸ – اموال غیرمنقول که اتباع خارجه در ایران بر طبق عهود تملک کرده یا می‌کنند از هر جهت تابع قوانین ایران خواهد بود.
ماده ۹ – مقررات عهودی که بر طبق قانون اساسی بین دولت ایران و سایر دول منعقد شده باشد در حکم قانون است.
ماده ۱۰ – قراردادهای خصوصی نسبت بکسانی که آن را منعقد نموده‌اند در صورتیکه مخالف صریح قانون نباشد نافذ است.
'''
question = "سکنه ایران و اتباع خارجه مطیع قوانین خارجه باید باشند؟"

# Tokenize the question
question_tokens = tokenizer(question, return_tensors="pt", padding="max_length", max_length=512, truncation=True)

# Initialize an empty list to store answers
answers = []

# Split the context into smaller parts
context_parts = [context[i:i+512] for i in range(0, len(context), 512)]

# Process each part of the context separately
for context_part in context_parts:
    # Concatenate the question and the current context part
    input_text = question + " " + context_part

    # Tokenize the combined input
    input_tokens = tokenizer(input_text, return_tensors="pt", padding="max_length", max_length=512, truncation=True)

    # Move tokens and model to GPU
    inputs = {key: value.to(device) for key, value in input_tokens.items()}
    model = model.to(device)

    # Perform question answering inference
    with torch.no_grad():
        outputs = model(**inputs)

    # Process the model's output to get the answer
    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits)
    answer = tokenizer.decode(input_tokens["input_ids"][0][answer_start:answer_end+1])

    # Append the answer to the list of answers
    answers.append(answer)

# Concatenate the answers if needed
final_answer = " ".join(answers)
final_answer = final_answer.strip('<s>').strip()
# Move the final answer to the CPU for further processing if needed
print(answer)
