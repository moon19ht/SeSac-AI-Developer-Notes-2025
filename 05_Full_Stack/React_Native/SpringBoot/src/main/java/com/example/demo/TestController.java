package com.example.demo;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController 
public class TestController {
	//http://127.0.0.1:9000/
	//포트번호수정은 src/main/resources/application.properties 파일에서 한다 
	@RequestMapping("/")
	String hello() {
		return "hello, spring boot";
	}
	
	@RequestMapping("/list")
	List<HashMap<String,String>> getList(){
		List<HashMap<String, String>> list 
		  = new ArrayList<HashMap<String, String>>();
		
		HashMap<String, String> map;
		for(int i=1; i<=20; i++)
		{
			map = new HashMap<String, String>();
			map.put("id", i+"");
			map.put("name", "홍길동"+i);
			map.put("phone", "phone"+i);
			map.put("email", "email"+i);
			list.add(map);
		}
		return list;
	}
}
