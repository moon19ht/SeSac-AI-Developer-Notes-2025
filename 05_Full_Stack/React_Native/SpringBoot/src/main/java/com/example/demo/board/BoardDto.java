package com.example.demo.board;

public class BoardDto {
	private String id="";
	private String title="";
	private String contents="";
	private String writer="";
	
	
	public BoardDto(String id, String title, String contents, String writer) {
		super();
		this.id = id;
		this.title = title;
		this.contents = contents;
		this.writer = writer;
	}
	
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getTitle() {
		return title;
	}
	public void setTitle(String title) {
		this.title = title;
	}
	public String getContents() {
		return contents;
	}
	public void setContents(String contents) {
		this.contents = contents;
	}
	public String getWriter() {
		return writer;
	}
	public void setWriter(String writer) {
		this.writer = writer;
	}
	
	
}
