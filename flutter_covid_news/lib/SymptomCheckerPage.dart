//part of covid_news;
// ignore_for_file: avoid_print

library covid_news;

import 'package:flutter/material.dart';
import 'main.dart';

class Page2 extends StatelessWidget {
  const Page2({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      /*appBar: AppBar(),
      body: const Center(
        child: Text('Page 2'),
      ),
    );
  }
}

class SymptomCheckerWidget extends StatefulWidget {
  const SymptomCheckerWidget({Key? key}) : super(key: key);

  @override
  _SymptomCheckerWidgetState createState() => _SymptomCheckerWidgetState();
}

class _SymptomCheckerWidgetState extends State<SymptomCheckerWidget> {
  String dropDownValue = "";
  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      key: scaffoldKey,*/
      appBar: AppBar(
        //backgroundColor: FlutterFlowTheme.of(context).primaryColor,
        automaticallyImplyLeading: false,
        /*leading: FFButtonWidget(
          onPressed: () async {
            await Navigator.push(
              context,
              PageTransition(
                type: PageTransitionType.fade,
                duration: Duration(milliseconds: 0),
                reverseDuration: Duration(milliseconds: 0),
                child: HomePageWidget(),
              ),
            );
          },
          text: 'Back',
          options: FFButtonOptions(
            width: 130,
            height: 40,
            color: FlutterFlowTheme.of(context).primaryColor,
            textStyle: FlutterFlowTheme.of(context).subtitle2.override(
                  fontFamily: 'Poppins',
                  color: Colors.white,
                ),
            borderSide: BorderSide(
              color: Colors.transparent,
              width: 1,
            ),
            borderRadius: 12,
          ),
        ),*/
        leading: TextButton(
          style: TextButton.styleFrom(
            padding: const EdgeInsets.all(16.0),
            primary: Colors.white,
            textStyle: const TextStyle(fontSize: 20),
          ),
          onPressed: () {
            //print("Back button");
            Navigator.of(context).push(_routeBackToMain());
          },
          child: const Text('Back'),
        ),
        title: Text(
          'Covid Symptom Checker',
          textAlign: TextAlign.center,
          /*style: FlutterFlowTheme.of(context).title2.override(
                fontFamily: 'Poppins',
                color: Colors.white,
                fontSize: 22,
              ),*/
        ),
        actions: [],
        centerTitle: false,
        elevation: 2,
      ),
      //backgroundColor: FlutterFlowTheme.of(context).primaryBackground,
      body: SafeArea(
        child: GestureDetector(
          onTap: () => FocusScope.of(context).unfocus(),
          child: Column(
            mainAxisSize: MainAxisSize.max,
            children: [
              Expanded(
                child: ListView(
                  padding: EdgeInsets.zero,
                  scrollDirection: Axis.vertical,
                  children: [
                    Row(
                      mainAxisSize: MainAxisSize.max,
                      mainAxisAlignment: MainAxisAlignment.center,
                      /*children: [
                        Text(
                          'Headache?',
                          //style: FlutterFlowTheme.of(context).bodyText1,
                        ),
                        /*FlutterFlowDropDown(
                          options: ['None', 'Mild', 'Severe'].toList(),
                          onChanged: (val) =>
                              setState(() => dropDownValue = val),
                          width: 180,
                          height: 50,
                          textStyle:
                              FlutterFlowTheme.of(context).bodyText1.override(
                                    fontFamily: 'Poppins',
                                    color: Colors.black,
                                  ),
                          hintText: 'Please select...',
                          fillColor: Colors.white,
                          elevation: 2,
                          borderColor: Colors.transparent,
                          borderWidth: 0,
                          borderRadius: 0,
                          margin: EdgeInsetsDirectional.fromSTEB(12, 4, 12, 4),
                          hidesUnderline: true,
                        ),*/
                      ],*/
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

Route _routeBackToMain() {
  return PageRouteBuilder(
    pageBuilder: (context, animation, secondaryAnimation) => const MyApp(),
    transitionsBuilder: (context, animation, secondaryAnimation, child) {
      return child;
    },
  );
}
