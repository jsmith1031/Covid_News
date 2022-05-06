//part of covid_news;
// ignore_for_file: avoid_print

library covid_news;

import 'dart:html' as html;

//import 'dart:ffi';

import 'package:flutter/material.dart';
import 'request.dart';
import 'dart:convert';

class articleStructure {
  String title = "";
  String body = "";
  String link = "";
  String logoLink = "";
  articleStructure(String title, String body, String link, String logoLink) {
    this.title = title;
    this.body = body;
    this.link = link;
    this.logoLink = logoLink;
  }
}

var articles = List<articleStructure>.empty(growable: true);
//var articles;
decodeMap(Map decoded, String source_name, String logoLink) {
  for (var word in decoded[source_name]) {
    //print(word['body']);
    //print(word['link']);
    print(word['title']);
    articleStructure article = new articleStructure(
        word['title'], word['body'], word['link'], logoLink);
    articles.add(article);
  }
}

Future testAsyncMethod() async {
  //print("HERE");
  String localHost = 'http://127.0.0.1:5000/';
  var data = await getData(Uri.parse(localHost));
  //var decodedData = jsonDecode(data);
  //print(decodedData['nbc_news']);
  Map decoded = jsonDecode(data);
  /*for (var word in decoded['nbc_news']) {
    //print(word['body']);
    //print(word['link']);
    print(word['title']);
    articleStructure article = new articleStructure(
        word['title'],
        word['body'],
        word['link'],
        "https://mlt.org/wp-content/uploads/2020/07/nbc-news-logo.png");
    articles.add(article);
  }*/
  decodeMap(decoded, 'nbc_news',
      "https://mlt.org/wp-content/uploads/2020/07/nbc-news-logo.png");
  decodeMap(decoded, 'fox_news',
      "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Fox_News_Channel_logo.svg/1920px-Fox_News_Channel_logo.svg.png");
}

class newsGridView extends StatelessWidget {
  const newsGridView({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    var newsArticleCardsList = List<Widget>.empty(growable: true);
    testAsyncMethod();
    for (int i = 0; i < articles.length; i++) {
      newsArticleCardsList.add(newsArticleCard(articles[i]));
      //print(i.toString());
    }
    return GridView(
      padding: EdgeInsets.zero,
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 3,
        crossAxisSpacing: 10,
        mainAxisSpacing: 10,
        childAspectRatio: 1,
      ),
      scrollDirection: Axis.vertical,
      /*children: [
        //newsArticleCard(),
      ],*/
      children: newsArticleCardsList,
    );
  }
}

class newsArticleCard extends StatelessWidget {
  /*const newsArticleCard(articleStructure a{
    Key? key,
  }) : super(key: key);*/
  articleStructure idk = new articleStructure(
    "",
    "",
    "",
    "",
  );
  newsArticleCard(articleStructure a) {
    this.idk = a;
  }
  @override
  Widget build(BuildContext context) {
    return Padding(
        padding: EdgeInsetsDirectional.fromSTEB(10, 10, 0, 0),
        /*
      GestureDetector(
        onTap: () => ......,
        child: Card(...),
      );

      */
        child: GestureDetector(
          onTap: () => html.window.open(idk.link, "News Article"),
          child: Card(
            //child: Card(
            clipBehavior: Clip.antiAliasWithSaveLayer,
            color: Color(0xFFF5F5F5),
            child: Column(
              mainAxisSize: MainAxisSize.max,
              children: [
                Row(
                  mainAxisSize: MainAxisSize.max,
                  mainAxisAlignment: MainAxisAlignment.start,
                  children: [
                    Padding(
                      padding: EdgeInsetsDirectional.fromSTEB(10, 10, 0, 0),
                      child: Image.network(
                        idk.logoLink,
                        //'https://picsum.photos/seed/100/600',
                        width: 50,
                        height: 50,
                        fit: BoxFit.cover,
                      ),
                    ),
                    Expanded(
                      child: Column(
                        mainAxisSize: MainAxisSize.max,
                        children: [
                          Padding(
                            padding:
                                EdgeInsetsDirectional.fromSTEB(10, 10, 10, 0),
                            child: Text(
                              //'This is the sample article title',
                              idk.title,
                              textAlign: TextAlign.center,
                              style: TextStyle(fontSize: 20),
                              /*style: FlutterFlowTheme.of(context)
                              .bodyText1
                              .override(
                                fontFamily: 'Poppins',
                                fontSize: 24,
                              ),*/
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
                Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(10, 10, 10, 10),
                  child: Text(
                    idk.body,
                    //'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                    //style: FlutterFlowTheme.of(context).bodyText1,
                    style: TextStyle(fontSize: 20),
                  ),
                ),
              ],
            ),
          ),
        ));
  }
}

//PLEASE DONT USE becuase it will make like 50 calls to the url in like 10ms and then get blocked depending how you use this
//PLEASE DONT USE becuase it will make like 50 calls to the url in like 10ms and then get blocked depending how you use this
//PLEASE DONT USE becuase it will make like 50 calls to the url in like 10ms and then get blocked depending how you use this
Image getTempImage() {
  return Image.network(
    'https://picsum.photos/seed/100/600',
    width: 50,
    height: 50,
    fit: BoxFit.cover,
  );
}

//PLEASE DONT USE becuase it will make like 50 calls to the url in like 10ms and then get blocked depending how you use this
//PLEASE DONT USE becuase it will make like 50 calls to the url in like 10ms and then get blocked depending how you use this
//PLEASE DONT USE becuase it will make like 50 calls to the url in like 10ms and then get blocked depending how you use this
Image getAbcNewsSourceLogo() {
  Image abcLogo = Image.network(
      //'https://w7.pngwing.com/pngs/142/945/png-transparent-abc-news-radio-new-york-city-breaking-news-others-text-logo-united-states-thumbnail.png'

      //images wont load from CORS domain
      //https://flutter.dev/docs/development/platform-integration/web-images
      'https://1000logos.net/wp-content/uploads/2021/10/ABC-logo-768x432.png',
      width: 50,
      height: 50,
      fit: BoxFit.scaleDown);
  return abcLogo;
}
