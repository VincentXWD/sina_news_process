import java.io.*;
import java.util.List;

import edu.stanford.nlp.ie.AbstractSequenceClassifier;
import edu.stanford.nlp.ie.crf.CRFClassifier;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.ling.CoreLabel;

public class process {

  public static void main(String[] args) throws IOException {
    String serializedClassifier = "res/english.all.3class.distsim.crf.ser.gz";
    AbstractSequenceClassifier<CoreLabel> classifier = CRFClassifier.getClassifierNoExceptions(serializedClassifier);

    BufferedInputStream fin = new BufferedInputStream(new FileInputStream("disworded_sina_news_with_attr.txt"));
    BufferedReader cin = new BufferedReader(new InputStreamReader(fin));
    BufferedWriter cout = new BufferedWriter (new FileWriter("disworded_sina_news_with_attr_handled.txt"));

    String s;
    while((s = cin.readLine()) != null) {
      List<List<CoreLabel>> out = classifier.classify(s);
      for (List<CoreLabel> sentence : out) {
        for (CoreLabel word : sentence) {
          if(word.get(CoreAnnotations.AnswerAnnotation.class).equals("O")) {
            cout.write(word.word()+' ');
          } else {
            cout.write(word.word()+'/'+word.get(CoreAnnotations.AnswerAnnotation.class)+' ');
          }
        }
        cout.write("\n");
      }
    }
  }
}

