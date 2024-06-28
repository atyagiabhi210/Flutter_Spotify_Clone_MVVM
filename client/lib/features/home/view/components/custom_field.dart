import 'package:flutter/material.dart';

class CustomTextField extends StatelessWidget {
 final String hintText;
 final TextEditingController controller;
 final bool isObscure;
 const CustomTextField({super.key, 
  required this.isObscure,
  required this.hintText,
  required this.controller});

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      validator: (val){
        if(val!.trim().isEmpty){
          return "$hintText is missing";
        }
        return null;
      },
      controller: controller,
      obscureText: isObscure,
      decoration:  InputDecoration(
        hintText: hintText
      ),

    );
  }
}