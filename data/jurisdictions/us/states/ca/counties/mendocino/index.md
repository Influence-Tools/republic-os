---
type: Jurisdiction
title: "Mendocino County, CA"
classification: county
fips: "06045"
state: "CA"
demographics:
  population: 90244
  population_under_18: 18897
  population_18_64: 49193
  population_65_plus: 22154
  median_household_income: 68092
  poverty_rate: 15.36
  homeownership_rate: 61.71
  unemployment_rate: 9.02
  median_home_value: 512200
  gini_index: 0.4809
  vacancy_rate: 16.4
  race_white: 58041
  race_black: 672
  race_asian: 1907
  race_native: 3209
  hispanic: 24941
  bachelors_plus: 22969
districts:
  - to: "us/states/ca/districts/02"
    rel: in-district
    area_weight: 0.9052
  - to: "us/states/ca/districts/senate/2"
    rel: in-district
    area_weight: 0.9063
  - to: "us/states/ca/districts/house/2"
    rel: in-district
    area_weight: 0.9063
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Mendocino County, CA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 90244 |
| Under 18 | 18897 |
| 18–64 | 49193 |
| 65+ | 22154 |
| Median household income | 68092 |
| Poverty rate | 15.36 |
| Homeownership rate | 61.71 |
| Unemployment rate | 9.02 |
| Median home value | 512200 |
| Gini index | 0.4809 |
| Vacancy rate | 16.4 |
| White | 58041 |
| Black | 672 |
| Asian | 1907 |
| Native | 3209 |
| Hispanic/Latino | 24941 |
| Bachelor's or higher | 22969 |

## Districts

- [CA-02](/us/states/ca/districts/02.md) — 91% (congressional)
- [CA Senate District 2](/us/states/ca/districts/senate/2.md) — 91% (state senate)
- [CA House District 2](/us/states/ca/districts/house/2.md) — 91% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
