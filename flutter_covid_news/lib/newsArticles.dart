//part of covid_news;
// ignore_for_file: avoid_print

library covid_news;

import 'package:flutter/material.dart';

//part 'newsArticles2.dart';
class newsArticles {
  String articleTitle = "";
  String articleText = "";
}

Container getArticle(BuildContext context) {
  print(MediaQuery.of(context).size.height);
  print(MediaQuery.of(context).size.height * 0.40);

  //build the scrollable grid view

  return Container(
    child:
        Text("Hello! i am inside a container!", style: TextStyle(fontSize: 20)),
    width: 0.3,
    height: MediaQuery.of(context).size.height * 0.40,
  );
}
