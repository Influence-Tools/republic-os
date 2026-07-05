---
type: Jurisdiction
title: "Harford County, MD"
classification: county
fips: "24025"
state: "MD"
demographics:
  population: 263757
  population_under_18: 58777
  population_18_64: 158964
  population_65_plus: 46016
  median_household_income: 112265
  poverty_rate: 7.14
  homeownership_rate: 79.66
  unemployment_rate: 3.83
  median_home_value: 386400
  gini_index: 0.408
  vacancy_rate: 3.48
  race_white: 192506
  race_black: 37734
  race_asian: 7949
  race_native: 523
  hispanic: 15290
  bachelors_plus: 106131
districts:
  - to: "us/states/md/districts/01"
    rel: in-district
    area_weight: 0.8572
  - to: "us/states/md/districts/senate/35"
    rel: in-district
    area_weight: 0.41
  - to: "us/states/md/districts/senate/34"
    rel: in-district
    area_weight: 0.2548
  - to: "us/states/md/districts/senate/7"
    rel: in-district
    area_weight: 0.1922
  - to: "us/states/md/districts/house/35a"
    rel: in-district
    area_weight: 0.41
  - to: "us/states/md/districts/house/34a"
    rel: in-district
    area_weight: 0.2207
  - to: "us/states/md/districts/house/7b"
    rel: in-district
    area_weight: 0.1921
  - to: "us/states/md/districts/house/34b"
    rel: in-district
    area_weight: 0.034
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Harford County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 263757 |
| Under 18 | 58777 |
| 18–64 | 158964 |
| 65+ | 46016 |
| Median household income | 112265 |
| Poverty rate | 7.14 |
| Homeownership rate | 79.66 |
| Unemployment rate | 3.83 |
| Median home value | 386400 |
| Gini index | 0.408 |
| Vacancy rate | 3.48 |
| White | 192506 |
| Black | 37734 |
| Asian | 7949 |
| Native | 523 |
| Hispanic/Latino | 15290 |
| Bachelor's or higher | 106131 |

## Districts

- [MD-01](/us/states/md/districts/01.md) — 86% (congressional)
- [MD Senate District 35](/us/states/md/districts/senate/35.md) — 41% (state senate)
- [MD Senate District 34](/us/states/md/districts/senate/34.md) — 25% (state senate)
- [MD Senate District 7](/us/states/md/districts/senate/7.md) — 19% (state senate)
- [MD House District 35A](/us/states/md/districts/house/35a.md) — 41% (state house)
- [MD House District 34A](/us/states/md/districts/house/34a.md) — 22% (state house)
- [MD House District 7B](/us/states/md/districts/house/7b.md) — 19% (state house)
- [MD House District 34B](/us/states/md/districts/house/34b.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
