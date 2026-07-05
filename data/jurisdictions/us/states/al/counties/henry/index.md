---
type: Jurisdiction
title: "Henry County, AL"
classification: county
fips: "01067"
state: "AL"
demographics:
  population: 17647
  population_under_18: 3602
  population_18_64: 9843
  population_65_plus: 4202
  median_household_income: 59931
  poverty_rate: 18.35
  homeownership_rate: 79.5
  unemployment_rate: 3.61
  median_home_value: 161000
  gini_index: 0.4858
  vacancy_rate: 23.36
  race_white: 12490
  race_black: 4430
  race_asian: 27
  race_native: 41
  hispanic: 390
  bachelors_plus: 3907
districts:
  - to: "us/states/al/districts/01"
    rel: in-district
    area_weight: 0.9961
  - to: "us/states/al/districts/senate/28"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/al/districts/house/85"
    rel: in-district
    area_weight: 0.9996
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Henry County, AL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 17647 |
| Under 18 | 3602 |
| 18–64 | 9843 |
| 65+ | 4202 |
| Median household income | 59931 |
| Poverty rate | 18.35 |
| Homeownership rate | 79.5 |
| Unemployment rate | 3.61 |
| Median home value | 161000 |
| Gini index | 0.4858 |
| Vacancy rate | 23.36 |
| White | 12490 |
| Black | 4430 |
| Asian | 27 |
| Native | 41 |
| Hispanic/Latino | 390 |
| Bachelor's or higher | 3907 |

## Districts

- [AL-01](/us/states/al/districts/01.md) — 100% (congressional)
- [AL Senate District 28](/us/states/al/districts/senate/28.md) — 100% (state senate)
- [AL House District 85](/us/states/al/districts/house/85.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
