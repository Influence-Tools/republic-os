---
type: Jurisdiction
title: "Cedar County, IA"
classification: county
fips: "19031"
state: "IA"
demographics:
  population: 18349
  population_under_18: 3875
  population_18_64: 10615
  population_65_plus: 3859
  median_household_income: 80602
  poverty_rate: 7.34
  homeownership_rate: 81.47
  unemployment_rate: 2.25
  median_home_value: 211300
  gini_index: 0.399
  vacancy_rate: 8.17
  race_white: 17238
  race_black: 79
  race_asian: 96
  race_native: 13
  hispanic: 507
  bachelors_plus: 3901
districts:
  - to: "us/states/ia/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ia/districts/senate/41"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ia/districts/house/82"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ia]
timestamp: "2026-07-03"
---

# Cedar County, IA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 18349 |
| Under 18 | 3875 |
| 18–64 | 10615 |
| 65+ | 3859 |
| Median household income | 80602 |
| Poverty rate | 7.34 |
| Homeownership rate | 81.47 |
| Unemployment rate | 2.25 |
| Median home value | 211300 |
| Gini index | 0.399 |
| Vacancy rate | 8.17 |
| White | 17238 |
| Black | 79 |
| Asian | 96 |
| Native | 13 |
| Hispanic/Latino | 507 |
| Bachelor's or higher | 3901 |

## Districts

- [IA-01](/us/states/ia/districts/01.md) — 100% (congressional)
- [IA Senate District 41](/us/states/ia/districts/senate/41.md) — 100% (state senate)
- [IA House District 82](/us/states/ia/districts/house/82.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
