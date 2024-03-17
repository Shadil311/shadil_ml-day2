{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Shadil311/shadil/blob/main/data_preprocessing.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "metadata": {
        "_uuid": "674378297bf7f78937a4f1aa466932e68466efcd",
        "id": "_R9SiXuZd1YL"
      },
      "cell_type": "markdown",
      "source": [
        "### Data Pre-processing Stage\n",
        "\n",
        "  This notebook contains the basic data pre processing steps.\n",
        "  * Preprocessing refers to the transformations applied to the data before feeding it to the machine learning algorithms.\n",
        "  * The data gathered from different sources is collected in raw format which is not feasible for the analysis.\n",
        "  * Data Preprocessing technique is used to convert the raw data into a clean data set."
      ]
    },
    {
      "metadata": {
        "_uuid": "fe10f16ae89b1e2579469abba5542de59d18ca7d",
        "id": "n39DDCJXd1YR"
      },
      "cell_type": "markdown",
      "source": [
        "#### Why preprocessing ?\n",
        "1. Real world data are generally\n",
        "    * Incomplete: lacking attribute values, lacking certain attributes of interest, or containing only aggregate data.\n",
        "    * Noisy: containing errors or outliers.\n",
        "    * Inconsistent: containing discrepancies in codes or names."
      ]
    },
    {
      "metadata": {
        "_uuid": "a30f7f7e2a855e2f0ef0bfc096bd4cc61a3399d9",
        "id": "1HPZpc4Ed1YS"
      },
      "cell_type": "markdown",
      "source": [
        "Let's take a sample dataset for this exercise.\n",
        "This dataset named \"data.csv\" contains whether a user purchased the product or not.\n",
        "The users data has age,salary and the country they belonged to."
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "3ed37978d39bc4b4497ed16fd66a99a40df07561",
        "id": "og1_0_DHd1YT"
      },
      "cell_type": "code",
      "source": [
        "###############################################################\n",
        "#       Step 1 : Importing the libraries                      #\n",
        "###############################################################\n",
        "\n",
        "\n",
        "# NumPy is module for Python. The name is an acronym for \"Numeric Python\" or \"Numerical Python\".\n",
        "# This makes sure that the precompiled mathematical and numerical functions\n",
        "# and functionalities of Numpy guarantee great execution speed.\n",
        "\n",
        "import numpy as np\n",
        "\n",
        "# Pandas is an open-source Python Library providing high-performance data manipulation\n",
        "# and analysis tool using its powerful data structures.\n",
        "# The name Pandas is derived from the word Panel Data – an Econometrics from Multidimensional data.\n",
        "\n",
        "import pandas as pd\n",
        "\n",
        "\n",
        "# The OS module in Python provides a way of using operating system dependent functionality.\n",
        "# The functions that the OS module provides allows you to interface with the underlying operating system\n",
        "# that Python is running on – be that Windows, Mac or Linux.\n",
        "\n",
        "import os"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "d09edc61b5ef258b23b6de01c4745613a4d00eca",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RDM1KRvDd1YV",
        "outputId": "44c00b52-78c6-426f-afe9-77772d236648"
      },
      "cell_type": "code",
      "source": [
        "###############################################################\n",
        "#       Step 2 : Importing the Dataset                        #\n",
        "###############################################################\n",
        "\n",
        "#Read the 'Data.csv' and store the data in the vairable dataset.\n",
        "dataset = pd.read_csv(\"preprocessing_data.csv\")\n",
        "print('Load the datasets...')\n",
        "\n",
        "\n",
        "# Print the shape of the dataset\n",
        "print ('dataset: %s'%(str(dataset.shape)))\n"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Load the datasets...\n",
            "dataset: (15, 4)\n"
          ]
        }
      ]
    },
    {
      "metadata": {
        "_uuid": "f2255fd0287097870845b0b4dbfd4e4ac04ea9f9",
        "id": "0T-5NVB0d1YW"
      },
      "cell_type": "markdown",
      "source": [
        "The dataset contains 15 rows and 4 columns"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "2764bded9c4328f4ca9902a333d882b12d09223e",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 520
        },
        "id": "BHRx-crqd1YX",
        "outputId": "1f199423-1fcb-44b5-fb2d-94af1896ada0"
      },
      "cell_type": "code",
      "source": [
        "# print the dataset\n",
        "dataset"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      Country   Age   Salary Purchased\n",
              "0       India  34.0  92000.0       Yes\n",
              "1   Sri lanka  22.0  25000.0       Yes\n",
              "2       China  31.0  74000.0       Yes\n",
              "3   Sri lanka  29.0      NaN        No\n",
              "4       China  55.0  98000.0       Yes\n",
              "5       India  24.0  30000.0        No\n",
              "6   Sri lanka  28.0  40000.0        No\n",
              "7       India   NaN  60000.0        No\n",
              "8       China  51.0  89000.0       Yes\n",
              "9       India  44.0  78000.0       Yes\n",
              "10  Sri lanka  21.0  20000.0        No\n",
              "11      China  25.0  30000.0       Yes\n",
              "12      India  33.0  45000.0       Yes\n",
              "13      India  42.0  65000.0       Yes\n",
              "14  Sri lanka  33.0  22000.0        No"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-6f2bc0f8-e92c-4a9e-aaf6-d5034897fdb9\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Country</th>\n",
              "      <th>Age</th>\n",
              "      <th>Salary</th>\n",
              "      <th>Purchased</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>India</td>\n",
              "      <td>34.0</td>\n",
              "      <td>92000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Sri lanka</td>\n",
              "      <td>22.0</td>\n",
              "      <td>25000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>China</td>\n",
              "      <td>31.0</td>\n",
              "      <td>74000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Sri lanka</td>\n",
              "      <td>29.0</td>\n",
              "      <td>NaN</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>China</td>\n",
              "      <td>55.0</td>\n",
              "      <td>98000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>India</td>\n",
              "      <td>24.0</td>\n",
              "      <td>30000.0</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>Sri lanka</td>\n",
              "      <td>28.0</td>\n",
              "      <td>40000.0</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>India</td>\n",
              "      <td>NaN</td>\n",
              "      <td>60000.0</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>China</td>\n",
              "      <td>51.0</td>\n",
              "      <td>89000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>India</td>\n",
              "      <td>44.0</td>\n",
              "      <td>78000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>Sri lanka</td>\n",
              "      <td>21.0</td>\n",
              "      <td>20000.0</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>China</td>\n",
              "      <td>25.0</td>\n",
              "      <td>30000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>India</td>\n",
              "      <td>33.0</td>\n",
              "      <td>45000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>India</td>\n",
              "      <td>42.0</td>\n",
              "      <td>65000.0</td>\n",
              "      <td>Yes</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>Sri lanka</td>\n",
              "      <td>33.0</td>\n",
              "      <td>22000.0</td>\n",
              "      <td>No</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-6f2bc0f8-e92c-4a9e-aaf6-d5034897fdb9')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-6f2bc0f8-e92c-4a9e-aaf6-d5034897fdb9 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-6f2bc0f8-e92c-4a9e-aaf6-d5034897fdb9');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-40c7c361-0c58-4372-9f7a-abf512153a1b\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-40c7c361-0c58-4372-9f7a-abf512153a1b')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-40c7c361-0c58-4372-9f7a-abf512153a1b button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_4ec7135b-f5b8-4981-b164-59e9c65f6530\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('dataset')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_4ec7135b-f5b8-4981-b164-59e9c65f6530 button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('dataset');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "dataset",
              "summary": "{\n  \"name\": \"dataset\",\n  \"rows\": 15,\n  \"fields\": [\n    {\n      \"column\": \"Country\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 3,\n        \"samples\": [\n          \"India\",\n          \"Sri lanka\",\n          \"China\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Age\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 10.593383794604076,\n        \"min\": 21.0,\n        \"max\": 55.0,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          33.0,\n          21.0,\n          34.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Salary\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 27980.36988499435,\n        \"min\": 20000.0,\n        \"max\": 98000.0,\n        \"num_unique_values\": 13,\n        \"samples\": [\n          65000.0,\n          20000.0,\n          92000.0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Purchased\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 2,\n        \"samples\": [\n          \"No\",\n          \"Yes\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "0b51a61e0f0b243b1b3c5650a30dcf02d6f943a5",
        "id": "S_Ewsthnd1YX"
      },
      "cell_type": "code",
      "source": [
        "# Separate the dependent and independent variables\n",
        "\n",
        "# Independent variable\n",
        "# iloc[rows,columns]\n",
        "# Take all rows\n",
        "# Take last but one column from the dataset (:-1)\n",
        "X = dataset.iloc[:,:-1].values\n",
        "\n",
        "# Dependent variable\n",
        "# iloc[rows,columns]\n",
        "# Take all rows\n",
        "# Take last column from the dataset (:-1)\n",
        "Y = dataset.iloc[:,3].values"
      ],
      "execution_count": 8,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "5351fbd6905b93aad9c455ee99cb0814e55cfc58",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ay1ypQGsd1YY",
        "outputId": "db27d5ee-9f83-4d16-9f54-76ebc9eafa7a"
      },
      "cell_type": "code",
      "source": [
        "# Print the X and Y\n",
        "print ('X: %s'%(str(X)))\n",
        "print ('-----------------------------------')\n",
        "print ('Y: %s'%(str(Y)))"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "X: [['India' 34.0 92000.0]\n",
            " ['Sri lanka' 22.0 25000.0]\n",
            " ['China' 31.0 74000.0]\n",
            " ['Sri lanka' 29.0 nan]\n",
            " ['China' 55.0 98000.0]\n",
            " ['India' 24.0 30000.0]\n",
            " ['Sri lanka' 28.0 40000.0]\n",
            " ['India' nan 60000.0]\n",
            " ['China' 51.0 89000.0]\n",
            " ['India' 44.0 78000.0]\n",
            " ['Sri lanka' 21.0 20000.0]\n",
            " ['China' 25.0 30000.0]\n",
            " ['India' 33.0 45000.0]\n",
            " ['India' 42.0 65000.0]\n",
            " ['Sri lanka' 33.0 22000.0]]\n",
            "-----------------------------------\n",
            "Y: ['Yes' 'Yes' 'Yes' 'No' 'Yes' 'No' 'No' 'No' 'Yes' 'Yes' 'No' 'Yes' 'Yes'\n",
            " 'Yes' 'No']\n"
          ]
        }
      ]
    },
    {
      "metadata": {
        "_uuid": "dffee0eb70165f04561442a9f05bf2fd0c0d205f",
        "id": "8kXErisAd1YZ"
      },
      "cell_type": "markdown",
      "source": [
        "#### 1. Handle Missing Data\n",
        "\n",
        "There are few missing data in the Age and salary columns (NaN values).\n",
        "\n",
        "#### i. Deleting Rows:\n",
        "*      We cannot remove the rows with the missing data as it will affect the output of the  machine learning algorithm.\n",
        "*      However we can delete a particular row if it has a null value for a particular feature and a particular column if it has more than 70-75% of missing values.\n",
        "      \n",
        "\n",
        "#### ii. Replacing With Mean/Median/Mode:\n",
        "*      This strategy can be applied on a feature which has numeric data like the age of a person.\n",
        "*      We can calculate the mean, median or mode of the feature and replace it with the missing values.    \n",
        "*     The loss of the data can be negated by this method which yields better results compared to removal of rows and  \n",
        "*       columns.\n",
        "*      Replacing with the above three approximations are a statistical approach of handling the missing values.\n",
        "*     This method is also called as leaking the data while training.\n",
        "*     Another way is to approximate it with the deviation of neighbouring values.\n",
        "*     This works better if the data is linear.\n"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "bc0f9fc1fde9aff85963ee3db02f1fd943d01d93",
        "id": "_vdx5XT4d1YZ"
      },
      "cell_type": "code",
      "source": [
        "###############################################################\n",
        "#       Step 3 : Missing Data                                 #\n",
        "###############################################################\n",
        "\n",
        "# Scikit-learn provides a range of supervised and unsupervised learning algorithms via a consistent interface in Python.\n",
        "# The sklearn.preprocessing package provides several common utility functions and transformer classes\n",
        "# to change raw feature vectors into a representation that is more suitable for the downstream estimators.\n",
        "\n",
        "from sklearn.impute import SimpleImputer\n",
        "\n",
        "# Imputer Class takes the follwing parameters:\n",
        "#     missing_values : The missing values in our dataset are called as NaN (Not a number).Default is NaN\n",
        "#     strategy       : replace the missing values by mean/median/mode. Default is mean.\n",
        "#     axis           : if axis = 0, we take we of the column and if axis = 1, we take mean value of row.\n",
        "\n",
        "imputer = SimpleImputer(missing_values =np.nan,strategy = 'mean')\n",
        "\n",
        "# Fit the imputer on X.\n",
        "# Take all rows and columns only with the missing values.\n",
        "# Note: Index starts with 0. Upper bound (3) is not included.\n",
        "\n",
        "# Fit imputer for columns 1 and 2 of X matrix.\n",
        "imputer.fit(X[:,1:3])\n",
        "\n",
        "#Replace missing data with mean of column\n",
        "X[:,1:3] = imputer.transform(X[:,1:3])\n"
      ],
      "execution_count": 10,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "cbb90e1ca86164287023c7fc38197bf087e0ef0e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OsSCfEHXd1Yc",
        "outputId": "fa955c86-748d-4a8c-91dd-f05f9c0ed2bf"
      },
      "cell_type": "code",
      "source": [
        "print ('X: %s'%(str(X)))"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "X: [['India' 34.0 92000.0]\n",
            " ['Sri lanka' 22.0 25000.0]\n",
            " ['China' 31.0 74000.0]\n",
            " ['Sri lanka' 29.0 54857.142857142855]\n",
            " ['China' 55.0 98000.0]\n",
            " ['India' 24.0 30000.0]\n",
            " ['Sri lanka' 28.0 40000.0]\n",
            " ['India' 33.714285714285715 60000.0]\n",
            " ['China' 51.0 89000.0]\n",
            " ['India' 44.0 78000.0]\n",
            " ['Sri lanka' 21.0 20000.0]\n",
            " ['China' 25.0 30000.0]\n",
            " ['India' 33.0 45000.0]\n",
            " ['India' 42.0 65000.0]\n",
            " ['Sri lanka' 33.0 22000.0]]\n"
          ]
        }
      ]
    },
    {
      "metadata": {
        "_uuid": "e06044bf541de146377c72fe4f34eb83100c2f49",
        "id": "1MZPtt2dd1Yd"
      },
      "cell_type": "markdown",
      "source": [
        "* Mean Value of Age    = Sum of all age values /14   = 33.714285714285715\n",
        "* Mean Value of Salary = Sum of all Salary value /14 = 54857.142857142855"
      ]
    },
    {
      "metadata": {
        "_uuid": "0504a7e75bde4ac7779062a37f144d9b9a096a17",
        "id": "6eJS49Zwd1Ye"
      },
      "cell_type": "markdown",
      "source": [
        "#### 2. Encode the Categorical data\n",
        "\n",
        "Categorical data are variables that contain label values rather than numeric values.\n",
        "Some algorithms can work with categorical data directly.\n",
        "\n",
        "For example, a decision tree can be learned directly from categorical data with no data transform required (this depends on the specific implementation).\n",
        "\n",
        "Many machine learning algorithms cannot operate on label data directly. They require all input variables and output variables to be numeric.\n",
        "\n",
        "This means that categorical data must be converted to a numerical form."
      ]
    },
    {
      "metadata": {
        "_uuid": "a8261920df0d266e0551cdae8264a07c96cdd7f8",
        "id": "MikSUpvVd1Yf"
      },
      "cell_type": "markdown",
      "source": [
        "In our dataset there are 2 columns with categorical data.\n",
        "\n",
        "The First column which contains the country and the last column purchased."
      ]
    },
    {
      "metadata": {
        "_uuid": "28a61d344d1556bdac352ac69e2ed0eb0e9a0cbc",
        "id": "IcmxAGGbd1Yg"
      },
      "cell_type": "markdown",
      "source": [
        "#### i.  Label Encoder:\n",
        "\n",
        "    * It is used to transform non-numerical labels to numerical labels (or nominal categorical variables).\n",
        "    * Numerical labels are always between 0 and n_classes-1.     \n",
        "\n",
        "#### ii. OneHotEncoder:\n",
        "    * Encode categorical integer features using a one-hot aka one-of-K scheme.\n",
        "    * The input to this transformer should be a matrix of integers, denoting the values taken on by categorical (discrete)\n",
        "      features.\n",
        "    * The output will be a sparse matrix where each column corresponds to one possible value of one feature.\n",
        "    * It is assumed that input features take on values in the range [0, n_values]\n",
        "    * This encoding is needed for feeding categorical data to many scikit-learn estimators, notably linear models and SVMs\n",
        "      with the standard kernels.        "
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "ad860887b31ba69dfe706ccd320b9cebe4fe931b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S31gjo_Fd1Yg",
        "outputId": "c3659d9c-744b-4895-fa7e-f08bea01148a"
      },
      "cell_type": "code",
      "source": [
        "###############################################################\n",
        "#       Step 4 : Categorical variables                        #\n",
        "###############################################################\n",
        "\n",
        "from sklearn.preprocessing import LabelEncoder,OneHotEncoder\n",
        "\n",
        "labelencoder_X = LabelEncoder()\n",
        "X[:,0] = labelencoder_X.fit_transform(X[:,0])\n",
        "X[:,0]"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1, 2, 0, 2, 0, 1, 2, 1, 0, 1, 2, 0, 1, 1, 2], dtype=object)"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "metadata": {
        "_uuid": "5f745a4a68c5e1d90dc1537940af301e69d9c164",
        "id": "YBS6CX1ud1Yh"
      },
      "cell_type": "markdown",
      "source": [
        "Now the categorical data of the country value is changed to numerical value.\n",
        "\n",
        "| Country | Value |\n",
        "|:--------|:------|\n",
        "| China   |   0   |  \n",
        "| India   |   1   |   \n",
        "| Srilanka|   2   |   \n"
      ]
    },
    {
      "metadata": {
        "_uuid": "9c4a6e53a3a028c11f1d9a91b9f45fbf8c64c996",
        "id": "WmaU6PqAd1Yi"
      },
      "cell_type": "markdown",
      "source": [
        "#### Dummy Encoding\n",
        "\n",
        "    * The above encoding will result in a problem.\n",
        "    * The label encoding transforms the data as shown in the table above.\n",
        "    * The Machine learning algorithm will assume that China>India>Sri Lanka.\n",
        "    * But this is not the case. We just converted the categorical value and assigned it to a numeric value.\n",
        "    * Hence there is a need to apply Dummy encoding to the above dataset.\n",
        "\n",
        "| Country | China | India | Sri Lanka |\n",
        "|:--------|:------|:------|:----------|\n",
        "| China   |   1   |  0    |    0      |   \n",
        "| India   |   0   |  1    |    0      |   \n",
        "| Srilanka|   0   |  0    |    1      |   \n",
        "| India   |   0   |  1    |    0      |  \n",
        "| Srilanka|   0   |  0    |    1      |  \n",
        "| China   |   1   |  0    |    0      |  \n",
        "  \n",
        "\n"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "2594e6f27a4b8a3fda17c7def917c1884546bae1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 180
        },
        "id": "bfclHnL2d1Yi",
        "outputId": "79a346a8-b797-4ffe-cbf9-26d9566ceb30"
      },
      "cell_type": "code",
      "source": [
        "# Applying the OneHotEncoder to the first column[0]\n",
        "onhotencoder = OneHotEncoder(categorical_features = [0])\n",
        "X=onhotencoder.fit_transform(X).toarray()\n"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "OneHotEncoder.__init__() got an unexpected keyword argument 'categorical_features'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-13-0eaef8ed3b22>\u001b[0m in \u001b[0;36m<cell line: 2>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# Applying the OneHotEncoder to the first column[0]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0monhotencoder\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mOneHotEncoder\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcategorical_features\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mX\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0monhotencoder\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfit_transform\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtoarray\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: OneHotEncoder.__init__() got an unexpected keyword argument 'categorical_features'"
          ]
        }
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "614c26108b7dcd141f65bf14b67e178aee962f19",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "31OreM6kd1Yj",
        "outputId": "8aff34a2-2d85-4b8c-d35a-ea618a5b2b44"
      },
      "cell_type": "code",
      "source": [
        "# Encoding the categorical data for Y matrix\n",
        "labelencoder_Y = LabelEncoder()\n",
        "Y = labelencoder_X.fit_transform(Y)\n",
        "Y"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0])"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "19b3d19ab1e4b1c1ff425d55b0eb79317bf7ab86",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 394
        },
        "id": "Ff3K3CCzd1Yk",
        "outputId": "9e98316d-2612-4377-b2e6-5aaf0fad0588"
      },
      "cell_type": "code",
      "source": [
        "###############################################################\n",
        "#       Step 5 : Splitting the dataset                        #\n",
        "###############################################################\n",
        "\n",
        "from sklearn.cross_validation import train_test_split\n",
        "\n",
        "# The test size is taken as 20% of the total dataset i.e., out of 15 only 3 rows are taken as test set\n",
        "X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 0)"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'sklearn.cross_validation'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-15-c9393cfaedab>\u001b[0m in \u001b[0;36m<cell line: 5>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;31m###############################################################\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcross_validation\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mtrain_test_split\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;31m# The test size is taken as 20% of the total dataset i.e., out of 15 only 3 rows are taken as test set\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'sklearn.cross_validation'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "780861983da7a12d75a1a3c7e6e03a1602d41c07",
        "scrolled": true,
        "id": "EsbO52Oid1Yk"
      },
      "cell_type": "code",
      "source": [
        "# Print the shape of the dataset\n",
        "print ('X_train: %s'%(str(X_train.shape)))\n",
        "print ('----------------')\n",
        "print ('X_test: %s'%(str(X_test.shape)))\n",
        "print ('----------------')\n",
        "print ('Y_train: %s'%(str(Y_train.shape)))\n",
        "print ('----------------')\n",
        "print ('Y_test: %s'%(str(Y_test.shape)))\n",
        "print ('----------------')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "0ef42f4efa7b7ed1f21966153a9a0de7a14d1d2e",
        "id": "gkymfdEmd1Yl"
      },
      "cell_type": "markdown",
      "source": [
        "#### 3. Scale your Features\n",
        "    *  Most of the times, the dataset will contain features highly varying in magnitudes, units and range.\n",
        "    *  Since the machine learning algorithms use Eucledian distance between two data points in their computations, this is\n",
        "       result in wrong prediction.\n",
        "      \n",
        "We need to put the variables in same range, in the same scale so that no variable dominates the other variable.     \n",
        "      \n",
        "      "
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "d7b0722d744c2da299c42cc2b6e50f6a21a87d20",
        "id": "qzXzFxkgd1Ym"
      },
      "cell_type": "code",
      "source": [
        "###############################################################\n",
        "#       Step 6 : Feature Scaling                              #\n",
        "###############################################################\n",
        "\n",
        "from sklearn.preprocessing import StandardScaler\n",
        "\n",
        "sc_X = StandardScaler()\n",
        "\n",
        "# We need to fit and transform the training set\n",
        "X_train = sc_X.fit_transform(X_train)\n",
        "\n",
        "# We need to fit the test set\n",
        "X_test = sc_X.transform(X_test)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "19edd09629c93a036a69dbb5adc2fa526c1403db",
        "id": "wwTbS6ZFd1Yn"
      },
      "cell_type": "code",
      "source": [
        "X_train"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "047b9e920be562717de782098c416e0bcc6e9bd5",
        "id": "GrClFSJ3d1Yo"
      },
      "cell_type": "code",
      "source": [
        "X_test"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "d884daf43f80af5c65844fbc763ea18c738890ec",
        "id": "scHWUdyid1Yo"
      },
      "cell_type": "markdown",
      "source": [
        "Now the all the data are in same scale. We can now apply different Machine learning model to the dataset."
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.6.6",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}