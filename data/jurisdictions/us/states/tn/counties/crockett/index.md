---
type: Jurisdiction
title: "Crockett County, TN"
classification: county
fips: "47033"
state: "TN"
demographics:
  population: 13944
  population_under_18: 3554
  population_18_64: 4231
  population_65_plus: 6159
  median_household_income: 62165
  poverty_rate: 14.52
  homeownership_rate: 71.62
  unemployment_rate: 2.89
  median_home_value: 158900
  gini_index: 0.4431
  vacancy_rate: 10.21
  race_white: 10070
  race_black: 1514
  race_asian: 62
  race_native: 117
  hispanic: 1585
  bachelors_plus: 2160
districts:
  - to: "us/states/tn/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tn/districts/senate/25"
    rel: in-district
    area_weight: 0.9992
  - to: "us/states/tn/districts/house/82"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tn]
timestamp: "2026-07-03"
---

# Crockett County, TN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13944 |
| Under 18 | 3554 |
| 18–64 | 4231 |
| 65+ | 6159 |
| Median household income | 62165 |
| Poverty rate | 14.52 |
| Homeownership rate | 71.62 |
| Unemployment rate | 2.89 |
| Median home value | 158900 |
| Gini index | 0.4431 |
| Vacancy rate | 10.21 |
| White | 10070 |
| Black | 1514 |
| Asian | 62 |
| Native | 117 |
| Hispanic/Latino | 1585 |
| Bachelor's or higher | 2160 |

## Districts

- [TN-08](/us/states/tn/districts/08.md) — 100% (congressional)
- [TN Senate District 25](/us/states/tn/districts/senate/25.md) — 100% (state senate)
- [TN House District 82](/us/states/tn/districts/house/82.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
