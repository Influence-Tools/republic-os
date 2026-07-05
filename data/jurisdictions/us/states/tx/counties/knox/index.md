---
type: Jurisdiction
title: "Knox County, TX"
classification: county
fips: "48275"
state: "TX"
demographics:
  population: 3307
  population_under_18: 859
  population_18_64: 1829
  population_65_plus: 619
  median_household_income: 56667
  poverty_rate: 15.74
  homeownership_rate: 77.37
  unemployment_rate: 1.28
  median_home_value: 77300
  gini_index: 0.4041
  vacancy_rate: 30.93
  race_white: 2251
  race_black: 162
  race_asian: 10
  race_native: 6
  hispanic: 1109
  bachelors_plus: 376
districts:
  - to: "us/states/tx/districts/13"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/senate/28"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/house/69"
    rel: in-district
    area_weight: 1.0
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Knox County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 3307 |
| Under 18 | 859 |
| 18–64 | 1829 |
| 65+ | 619 |
| Median household income | 56667 |
| Poverty rate | 15.74 |
| Homeownership rate | 77.37 |
| Unemployment rate | 1.28 |
| Median home value | 77300 |
| Gini index | 0.4041 |
| Vacancy rate | 30.93 |
| White | 2251 |
| Black | 162 |
| Asian | 10 |
| Native | 6 |
| Hispanic/Latino | 1109 |
| Bachelor's or higher | 376 |

## Districts

- [TX-13](/us/states/tx/districts/13.md) — 100% (congressional)
- [TX Senate District 28](/us/states/tx/districts/senate/28.md) — 100% (state senate)
- [TX House District 69](/us/states/tx/districts/house/69.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
