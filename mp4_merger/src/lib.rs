use pyo3::prelude::*;
use std::path::Path;
use mp4_merge::join_files;

#[pyfunction]
fn merge_videos(input_files: Vec<String>, output_file: String) -> PyResult<()> {
    // Convert the Vec<String> into Vec<&str>
    let input_refs: Vec<&str> = input_files.iter().map(|s| s.as_str()).collect();
    let result = join_files(&input_refs, &output_file.as_str(), |progress| {
        println!("Merging... {:.2}%", progress * 100.0);
    });

    // Check the result for success or failure
    match result {
        Ok(_) => Ok(()),
        Err(e) => Err(pyo3::exceptions::PyRuntimeError::new_err(format!("Failed to merge videos: {}", e))),
    }
}

#[pymodule]
fn mp4_merger(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(merge_videos, m)?)?;
    Ok(())
}
