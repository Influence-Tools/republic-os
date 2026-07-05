---
type: Jurisdiction
title: "Bullock County, AL"
classification: county
fips: "01011"
state: "AL"
demographics:
  population: 10058
  population_under_18: 2068
  population_18_64: 6123
  population_65_plus: 1867
  median_household_income: 31310
  poverty_rate: 33.27
  homeownership_rate: 66.65
  unemployment_rate: 7.22
  median_home_value: 81700
  gini_index: 0.5067
  vacancy_rate: 19.46
  race_white: 2293
  race_black: 6986
  race_asian: 42
  race_native: 0
  hispanic: 602
  bachelors_plus: 793
districts:
  - to: "us/states/al/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/al/districts/senate/28"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/al/districts/house/84"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Bullock County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10058 |
| Under 18 | 2068 |
| 18–64 | 6123 |
| 65+ | 1867 |
| Median household income | 31310 |
| Poverty rate | 33.27 |
| Homeownership rate | 66.65 |
| Unemployment rate | 7.22 |
| Median home value | 81700 |
| Gini index | 0.5067 |
| Vacancy rate | 19.46 |
| White | 2293 |
| Black | 6986 |
| Asian | 42 |
| Native | 0 |
| Hispanic/Latino | 602 |
| Bachelor's or higher | 793 |

## Districts

- [AL-02](/us/states/al/districts/02.md) — 100% (congressional)
- [AL Senate District 28](/us/states/al/districts/senate/28.md) — 100% (state senate)
- [AL House District 84](/us/states/al/districts/house/84.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
