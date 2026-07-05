---
type: Jurisdiction
title: "Taylor County, FL"
classification: county
fips: "12123"
state: "FL"
demographics:
  population: 21503
  population_under_18: 4365
  population_18_64: 12570
  population_65_plus: 4568
  median_household_income: 49073
  poverty_rate: 17.34
  homeownership_rate: 76.0
  unemployment_rate: 5.39
  median_home_value: 114600
  gini_index: 0.5139
  vacancy_rate: 29.16
  race_white: 15591
  race_black: 4142
  race_asian: 132
  race_native: 105
  hispanic: 919
  bachelors_plus: 3225
districts:
  - to: "us/states/fl/districts/02"
    rel: in-district
    area_weight: 0.6961
  - to: "us/states/fl/districts/senate/3"
    rel: in-district
    area_weight: 0.6974
  - to: "us/states/fl/districts/house/7"
    rel: in-district
    area_weight: 0.6974
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Taylor County, FL

County jurisdiction — 22 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 21503 |
| Under 18 | 4365 |
| 18–64 | 12570 |
| 65+ | 4568 |
| Median household income | 49073 |
| Poverty rate | 17.34 |
| Homeownership rate | 76.0 |
| Unemployment rate | 5.39 |
| Median home value | 114600 |
| Gini index | 0.5139 |
| Vacancy rate | 29.16 |
| White | 15591 |
| Black | 4142 |
| Asian | 132 |
| Native | 105 |
| Hispanic/Latino | 919 |
| Bachelor's or higher | 3225 |

## Districts

- [FL-02](/us/states/fl/districts/02.md) — 70% (congressional)
- [FL Senate District 3](/us/states/fl/districts/senate/3.md) — 70% (state senate)
- [FL House District 7](/us/states/fl/districts/house/7.md) — 70% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
