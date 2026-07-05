---
type: Jurisdiction
title: "Martin County, IN"
classification: county
fips: "18101"
state: "IN"
demographics:
  population: 9830
  population_under_18: 2139
  population_18_64: 5628
  population_65_plus: 2063
  median_household_income: 68594
  poverty_rate: 16.28
  homeownership_rate: 78.51
  unemployment_rate: 2.39
  median_home_value: 159400
  gini_index: 0.4196
  vacancy_rate: 14.82
  race_white: 9393
  race_black: 35
  race_asian: 12
  race_native: 3
  hispanic: 142
  bachelors_plus: 1183
districts:
  - to: "us/states/in/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/39"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/in/districts/house/63"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Martin County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 9830 |
| Under 18 | 2139 |
| 18–64 | 5628 |
| 65+ | 2063 |
| Median household income | 68594 |
| Poverty rate | 16.28 |
| Homeownership rate | 78.51 |
| Unemployment rate | 2.39 |
| Median home value | 159400 |
| Gini index | 0.4196 |
| Vacancy rate | 14.82 |
| White | 9393 |
| Black | 35 |
| Asian | 12 |
| Native | 3 |
| Hispanic/Latino | 142 |
| Bachelor's or higher | 1183 |

## Districts

- [IN-08](/us/states/in/districts/08.md) — 100% (congressional)
- [IN Senate District 39](/us/states/in/districts/senate/39.md) — 100% (state senate)
- [IN House District 63](/us/states/in/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
