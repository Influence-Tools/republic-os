---
type: Jurisdiction
title: "Ohio County, IN"
classification: county
fips: "18115"
state: "IN"
demographics:
  population: 5999
  population_under_18: 1196
  population_18_64: 3390
  population_65_plus: 1413
  median_household_income: 70392
  poverty_rate: 8.1
  homeownership_rate: 81.33
  unemployment_rate: 1.35
  median_home_value: 213100
  gini_index: 0.3873
  vacancy_rate: 5.42
  race_white: 5687
  race_black: 5
  race_asian: 64
  race_native: 7
  hispanic: 112
  bachelors_plus: 1009
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 0.9986
  - to: "us/states/in/districts/senate/43"
    rel: in-district
    area_weight: 0.9993
  - to: "us/states/in/districts/house/68"
    rel: in-district
    area_weight: 0.9993
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Ohio County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 5999 |
| Under 18 | 1196 |
| 18–64 | 3390 |
| 65+ | 1413 |
| Median household income | 70392 |
| Poverty rate | 8.1 |
| Homeownership rate | 81.33 |
| Unemployment rate | 1.35 |
| Median home value | 213100 |
| Gini index | 0.3873 |
| Vacancy rate | 5.42 |
| White | 5687 |
| Black | 5 |
| Asian | 64 |
| Native | 7 |
| Hispanic/Latino | 112 |
| Bachelor's or higher | 1009 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 43](/us/states/in/districts/senate/43.md) — 100% (state senate)
- [IN House District 68](/us/states/in/districts/house/68.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
