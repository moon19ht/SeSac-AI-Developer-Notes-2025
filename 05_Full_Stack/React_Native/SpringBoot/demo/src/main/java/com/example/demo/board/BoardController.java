package com.example.demo.board;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class BoardController {
	@Autowired 
	BoardDao boardDao;
	
	@RequestMapping("/board/list")
	List<BoardDto> getList(){
		return boardDao.getList();
	}
	
	//http://127.0.0.1:9000/board/getView/1
	@RequestMapping("/board/getView/{id}")
	BoardDto getView(String id){
		return boardDao.getView(id);
	}
	
	@RequestMapping("/board/insert/")
	void insert(BoardDto dto)
	{
		boardDao.insert(dto);
	}
}
