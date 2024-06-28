import 'package:client/core/theme/theme.dart';
import 'package:client/features/home/view/screens/signup_screen.dart';
import 'package:flutter/material.dart';

void main(){
  runApp(myApp());

}

class myApp extends StatelessWidget{
  @override
  Widget build(BuildContext context) {
    
    return  MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: AppTheme.darkThemeMode,
      home:const SignUpScreen(),
    );
  }
}