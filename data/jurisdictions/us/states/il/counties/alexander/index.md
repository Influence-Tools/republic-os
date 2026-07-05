---
type: Jurisdiction
title: "Alexander County, IL"
classification: county
fips: "17003"
state: "IL"
demographics:
  population: 4875
  population_under_18: 1040
  population_18_64: 2620
  population_65_plus: 1215
  median_household_income: 47043
  poverty_rate: 19.02
  homeownership_rate: 77.57
  unemployment_rate: 6.48
  median_home_value: 59800
  gini_index: 0.4803
  vacancy_rate: 35.19
  race_white: 3069
  race_black: 1616
  race_asian: 21
  race_native: 0
  hispanic: 33
  bachelors_plus: 599
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/il/districts/house/118"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Alexander County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4875 |
| Under 18 | 1040 |
| 18–64 | 2620 |
| 65+ | 1215 |
| Median household income | 47043 |
| Poverty rate | 19.02 |
| Homeownership rate | 77.57 |
| Unemployment rate | 6.48 |
| Median home value | 59800 |
| Gini index | 0.4803 |
| Vacancy rate | 35.19 |
| White | 3069 |
| Black | 1616 |
| Asian | 21 |
| Native | 0 |
| Hispanic/Latino | 33 |
| Bachelor's or higher | 599 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL House District 118](/us/states/il/districts/house/118.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
