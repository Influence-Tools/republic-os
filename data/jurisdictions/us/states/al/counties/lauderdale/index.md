---
type: Jurisdiction
title: "Lauderdale County, AL"
classification: county
fips: "01077"
state: "AL"
demographics:
  population: 95830
  population_under_18: 18584
  population_18_64: 57601
  population_65_plus: 19645
  median_household_income: 62649
  poverty_rate: 12.16
  homeownership_rate: 68.9
  unemployment_rate: 4.06
  median_home_value: 200300
  gini_index: 0.4601
  vacancy_rate: 12.64
  race_white: 79408
  race_black: 8774
  race_asian: 595
  race_native: 317
  hispanic: 3317
  bachelors_plus: 26918
districts:
  - to: "us/states/al/districts/04"
    rel: in-district
    area_weight: 0.7171
  - to: "us/states/al/districts/05"
    rel: in-district
    area_weight: 0.2826
  - to: "us/states/al/districts/senate/1"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/al/districts/house/1"
    rel: in-district
    area_weight: 0.5129
  - to: "us/states/al/districts/house/2"
    rel: in-district
    area_weight: 0.3503
  - to: "us/states/al/districts/house/3"
    rel: in-district
    area_weight: 0.1365
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, al]
timestamp: "2026-07-03"
---

# Lauderdale County, AL

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 95830 |
| Under 18 | 18584 |
| 18–64 | 57601 |
| 65+ | 19645 |
| Median household income | 62649 |
| Poverty rate | 12.16 |
| Homeownership rate | 68.9 |
| Unemployment rate | 4.06 |
| Median home value | 200300 |
| Gini index | 0.4601 |
| Vacancy rate | 12.64 |
| White | 79408 |
| Black | 8774 |
| Asian | 595 |
| Native | 317 |
| Hispanic/Latino | 3317 |
| Bachelor's or higher | 26918 |

## Districts

- [AL-04](/us/states/al/districts/04.md) — 72% (congressional)
- [AL-05](/us/states/al/districts/05.md) — 28% (congressional)
- [AL Senate District 1](/us/states/al/districts/senate/1.md) — 100% (state senate)
- [AL House District 1](/us/states/al/districts/house/1.md) — 51% (state house)
- [AL House District 2](/us/states/al/districts/house/2.md) — 35% (state house)
- [AL House District 3](/us/states/al/districts/house/3.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
