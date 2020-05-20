To do a BERT based multi classification analysis I have followed this [ Medium tutorial](https://towardsdatascience.com/beginners-guide-to-bert-for-multi-classification-task-92f5445c2d7c) for setup and installation, data set preparation and training.   

**Steps:**
1. Download the Tensor Flow Code and pre-trained model by cloning the repository from the following [link](https://github.com/google-research/bert)
2. BERT model: I have used a BERT-base uncased model ( 12-layer, 768-hidden, 12-heads , 110M parameters) as in the tutorial due to limited local storage and computation capacity
3. Dataset preparation: created a dataset folder with `train.tsv`, `test.tsv` and `dev.tsv` in the tutorial specified format using pandas and sklearn. I did a 80:10:10 train, test, dev split. The text is completely unprocessed. The labels were hot encoded using sklearn LabelEncoder. 
4. Training Model: I have also used the ColaProcessor as in the tutorial. To adapt the code for multilabel classifcation we modify `get_labels()` function of ColaProcessor Class from ["0", "1"] to add the other levels (0-8 in this case). 
5. Parameter tuning: keeping the other parameters same as tutorial, I changed `max_seq_length` to 256 (from default 128) to accomodate a longer texts.


**Shell Command for Training:**
`CUDA_VISIBLE_DEVICES=0 python run_classifier.py --task_name=cola --do_train=true --do_eval=true --data_dir=./dataset --vocab_file=./model/vocab.txt --bert_config_file=./model/bert_config.json --init_checkpoint=./model/bert_model.ckpt --max_seq_length=256 --train_batch_size=2 --learning_rate=2e-5 --num_train_epochs=3.0 --output_dir=./bert_output/ --do_lower_case=False --save_checkpoints_steps 10000`

**Evaluation Results:**
eval_accuracy = 0.5265151
eval_loss = 1.5367126
global_step = 9498
loss = 1.5367126

**Shell command for Prediction:**
`CUDA_VISIBLE_DEVICES=0 python run_classifier.py --task_name=cola --do_predict=true --data_dir=./dataset --vocab_file=./model/vocab.txt --bert_config_file=./model/bert_config.json --init_checkpoint=./bert_output/model.ckpt-236962 --max_seq_length=256 --output_dir=./bert_output/`


**Conclusion:**
The BERT model did not perform with sufficiently high accuracy. It is unclear what could be causing such poor performace but could be potentially attributed to less class-wise training data among other reasons. 
