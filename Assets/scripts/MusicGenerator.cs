using UnityEngine;
using System.Collections;
using System.IO;

public class MusicGenerator : MonoBehaviour {

	private string convertURL = "http://lilypond.pythonanywhere.com/";

	void Start () {
		turnLilypondFileToSheet();
	}


	void Update () {
	
	}

	public void turnLilypondFileToSheet(){
		string path = "";
		if(Application.platform == RuntimePlatform.IPhonePlayer){
			path = Application.dataPath + "/Raw";
		}else if(Application.platform == RuntimePlatform.Android){
			path = "jar:file://" + Application.dataPath + "!/assets/";
		}else{
			path = Application.dataPath + "/StreamingAssets";
		}
			
		string filepath = path + "/Test.ly";
		string savepath = path + "/Sheet.pdf";

		string url = convertURL;

		WWWForm form = new WWWForm();
		form.AddField("external","external");

		if (File.Exists(filepath))
		{
			print("exists");
			FileStream stream = new FileStream(filepath, FileMode.Open, FileAccess.Read, FileShare.Read);
			BinaryReader reader = new BinaryReader(stream);
			form.AddBinaryData("file", reader.ReadBytes((int)reader.BaseStream.Length),"Test.ly"); // 1
			stream.Close();
		}

		byte[] bytes;

		StartCoroutine(waitForRequest(url,form,(www) => {
			bytes = www.bytes;
			System.IO.File.WriteAllBytes(savepath, bytes);
		}));

	}

	private IEnumerator waitForRequest(string url, WWWForm form,System.Action<WWW> complete){
		WWW www = new WWW(url,form);
		yield return www;
		complete(www);
		// check for errors
		if (www.error == null)
		{
			Debug.Log("WWW Ok!: " + www.text);
		} else {
			Debug.Log("WWW Error: "+ www.error);
		}
	}
}
