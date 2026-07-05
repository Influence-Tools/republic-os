---
type: Jurisdiction
title: "Crockett County, TX"
classification: county
fips: "48105"
state: "TX"
demographics:
  population: 2822
  population_under_18: 746
  population_18_64: 1539
  population_65_plus: 537
  median_household_income: 81022
  poverty_rate: 9.32
  homeownership_rate: 73.71
  unemployment_rate: 3.01
  gini_index: 0.3742
  vacancy_rate: 29.15
  race_white: 930
  race_black: 7
  race_asian: 0
  race_native: 0
  hispanic: 1886
  bachelors_plus: 321
districts:
  - to: "us/states/tx/districts/23"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/tx/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/tx/districts/house/53"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Crockett County, TX

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2822 |
| Under 18 | 746 |
| 18–64 | 1539 |
| 65+ | 537 |
| Median household income | 81022 |
| Poverty rate | 9.32 |
| Homeownership rate | 73.71 |
| Unemployment rate | 3.01 |
| Gini index | 0.3742 |
| Vacancy rate | 29.15 |
| White | 930 |
| Black | 7 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 1886 |
| Bachelor's or higher | 321 |

## Districts

- [TX-23](/us/states/tx/districts/23.md) — 100% (congressional)
- [TX Senate District 19](/us/states/tx/districts/senate/19.md) — 100% (state senate)
- [TX House District 53](/us/states/tx/districts/house/53.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
