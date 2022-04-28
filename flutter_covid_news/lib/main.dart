//library covid_news;

import 'package:flutter/material.dart';
import 'newsArticles.dart';
import 'appTopBar.dart';
import 'SymptomCheckerPage.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Covid News',
      theme: ThemeData(
        primarySwatch: Colors.teal,
      ),
      home: HomePageWidget(),
    );
  }
}

class HomePageWidget extends StatefulWidget {
  const HomePageWidget({Key? key}) : super(key: key);

  @override
  _HomePageWidgetState createState() => _HomePageWidgetState();
}

class _HomePageWidgetState extends State<HomePageWidget> {
  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: scaffoldKey,
      //backgroundColor: FlutterFlowTheme.of(context).primaryBackground,
      body: GestureDetector(
        onTap: () => FocusScope.of(context).unfocus(),
        child: Column(
          mainAxisSize: MainAxisSize.max,
          children: [
            Row(
              mainAxisSize: MainAxisSize.max,
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(4, 4, 0, 0),
                  child: topBarButton(),
                ),
                Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(4, 4, 4, 0),
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(4),
                    child: Stack(
                      children: <Widget>[
                        Positioned.fill(
                          child: Container(
                            decoration: const BoxDecoration(
                              gradient: LinearGradient(
                                colors: <Color>[
                                  Color(0xFF0D47A1),
                                  Color(0xFF1976D2),
                                  Color(0xFF42A5F5),
                                ],
                              ),
                            ),
                          ),
                        ),
                        TextButton(
                          style: TextButton.styleFrom(
                            padding: const EdgeInsets.all(16.0),
                            primary: Colors.white,
                            textStyle: const TextStyle(fontSize: 20),
                          ),
                          //onPressed: () {
                          //print('Symptom Checker');
                          //},
                          /*onPressed: () async {
                            await Navigator.push(
                              //context,
                              /*PageTransition(
                              type: PageTransitionType.fade,
                              duration: Duration(milliseconds: 0),
                              reverseDuration: Duration(milliseconds: 0),
                              child: SymptomCheckerWidget(),
                            ),*/
                            )
                          },*/
                          onPressed: () {
                            Navigator.of(context).push(_createRoute());
                          },
                          child: const Text('Symptom Checker'),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
            Divider(),
            Row(
              mainAxisSize: MainAxisSize.max,
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(50, 0, 0, 0),
                  child: Text(
                    'Recent Covid News',
                    //style: FlutterFlowTheme.of(context).bodyText1,
                    style: TextStyle(fontSize: 14),
                  ),
                ),
                Padding(
                  padding: EdgeInsetsDirectional.fromSTEB(0, 0, 50, 0),
                  /*child: FlutterFlowAdBanner(
                    width: MediaQuery.of(context).size.width * 0.6,
                    height: 50,
                    showsTestAd: true,
                  ),*/
                ),
              ],
            ),
            Expanded(
              child:
                  newsGridView(), //This is the scrollable grid view where all the news articles live
            ),
          ],
        ),
      ),
    );
  }
}

class newsGridView extends StatelessWidget {
  const newsGridView({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return GridView(
      padding: EdgeInsets.zero,
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 3,
        crossAxisSpacing: 10,
        mainAxisSpacing: 10,
        childAspectRatio: 1,
      ),
      scrollDirection: Axis.vertical,
      children: [
        Padding(
          padding: EdgeInsetsDirectional.fromSTEB(10, 10, 0, 0),
          child: Card(
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
                        'https://picsum.photos/seed/100/600',
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
                              'This is the sample article title',
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
                    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
                    //style: FlutterFlowTheme.of(context).bodyText1,
                    style: TextStyle(fontSize: 20),
                  ),
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }
}

class topBarButton extends StatelessWidget {
  const topBarButton({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ClipRRect(
      borderRadius: BorderRadius.circular(4),
      child: Stack(
        children: <Widget>[
          Positioned.fill(
            child: Container(
              decoration: const BoxDecoration(
                gradient: LinearGradient(
                  colors: <Color>[
                    Color(0xFF0D47A1),
                    Color(0xFF1976D2),
                    Color(0xFF42A5F5),
                  ],
                ),
              ),
            ),
          ),
          TextButton(
            style: TextButton.styleFrom(
              padding: const EdgeInsets.all(16.0),
              primary: Colors.white,
              textStyle: const TextStyle(fontSize: 20),
            ),
            onPressed: () {
              print('Checking Local News');
            },
            child: const Text('Check Local News'),
          ),
        ],
      ),
    );
  }
}

Route _createRoute() {
  return PageRouteBuilder(
    pageBuilder: (context, animation, secondaryAnimation) => const Page2(),
    transitionsBuilder: (context, animation, secondaryAnimation, child) {
      return child;
    },
  );
}
/*
class Page2 extends StatelessWidget {
  const Page2({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: const Center(
        child: Text('Page 2'),
      ),
    );
  }
}

*/
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////
/*
import 'package:flutter/material.dart';
import 'newsArticles.dart';
import 'appTopBar.dart';
//import 'lib/library.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  void switchScreen() {
    //setState(() {
    // This call to setState tells the Flutter framework that something has
    // changed in this State, which causes it to rerun the build method below
    // so that the display can reflect the updated values. If we changed
    // _counter without calling setState(), then the build method would not be
    // called again, and so nothing would appear to happen.
  }

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    //print(MediaQuery.of(context).size.height);
    //print(MediaQuery.of(context).size.width);
    return MaterialApp(
      title: 'Covid News',
      theme: ThemeData(
        primarySwatch: Colors.teal,
      ),
      //home: const MyHomePage(title: 'Covid News Home Page'),
      home: MyStatelessWidget(),
      /*     switchToScreen: FloatingActionButton(
        onPressed: switchScreen(),
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),*/
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key, required this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;
  void _incrementCounter() {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.

    return Scaffold(
      appBar: AppBar(
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        child: //getArticle(context)),
            Column(
          children: <Widget>[
            Container(
              child: getNewsSourceLogo(),
            ),
            /*Container(
              child: Text(
                'Welcome to Prime Message',
                textAlign: TextAlign.center,
                style: TextStyle(
                    fontFamily: 'Aleo',
                    fontStyle: FontStyle.normal,
                    fontWeight: FontWeight.bold,
                    fontSize: 25.0,
                    color: Colors.black),
              ),
            ),*/
          ],
        ),
      ),
      //body: Center(child: newsArticlesTable(context)),
    );

    //return TableCreation();
  }

  Column newsArticlesTable(BuildContext context) {
    return Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Container(
            margin: EdgeInsets.all(10),
            child: Table(
              border: TableBorder.all(width: 0),
              children: [
                TableRow(children: [
                  Text('Article 1',
                      textAlign: TextAlign.center,
                      style: TextStyle(fontWeight: FontWeight.bold)),
                  Text('Article 2',
                      textAlign: TextAlign.center,
                      style: TextStyle(fontWeight: FontWeight.bold)),
                  builtArticle(context),
                ]),
                TableRow(children: [
                  Text('Article 4', textAlign: TextAlign.center),
                  getNewsSourceLogo(),
                  //Text('Article 6', textAlign: TextAlign.center),
                  builtArticle(context),
                ]),
              ],
            ),
          ),
        ]);
  }
}

Image getNewsSourceLogo() {
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

Container builtArticle(BuildContext context) {
  print(MediaQuery.of(context).size.height);
  print(MediaQuery.of(context).size.height * 0.40);
  return Container(
    child:
        Text("Hello! i am inside a container!", style: TextStyle(fontSize: 20)),
    width: 0.3,
    height: MediaQuery.of(context).size.height * 0.40,
  );
}
*/