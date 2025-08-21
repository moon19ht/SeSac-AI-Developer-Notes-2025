package com.example.demo.board;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

@Repository
public class BoardDao {
	List<BoardDto> list = new ArrayList<BoardDto>();

	public BoardDao() {
		for(int i=1; i<=50; i++)
			list.add(new BoardDto(i+"",
					"제목"+i, "내용"+i, "작성자"+i));
	}
	
	public List<BoardDto> getList()
	{
		return list;
	}
	
	public void insert(BoardDto dto)
	{
		list.add(dto);
	}
	
	public BoardDto getView(String id) {
		return list.get(list.indexOf(id));
	}
}



