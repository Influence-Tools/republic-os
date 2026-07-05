---
type: Jurisdiction
title: "Kalawao County, HI"
classification: county
fips: "15005"
state: "HI"
demographics:
  population: 67
  population_65_plus: 14
  median_household_income: 73750
  poverty_rate: 22.73
  homeownership_rate: 0.0
  unemployment_rate: 0.0
  gini_index: 0.2834
  vacancy_rate: 62.62
  race_white: 19
  race_black: 0
  race_asian: 12
  race_native: 12
  hispanic: 9
  bachelors_plus: 24
districts:
  - to: "us/states/hi/districts/02"
    rel: in-district
    area_weight: 0.2466
  - to: "us/states/hi/districts/senate/7"
    rel: in-district
    area_weight: 0.2307
  - to: "us/states/hi/districts/house/13"
    rel: in-district
    area_weight: 0.2307
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, hi]
timestamp: "2026-07-03"
---

# Kalawao County, HI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67 |
| 65+ | 14 |
| Median household income | 73750 |
| Poverty rate | 22.73 |
| Homeownership rate | 0.0 |
| Unemployment rate | 0.0 |
| Gini index | 0.2834 |
| Vacancy rate | 62.62 |
| White | 19 |
| Black | 0 |
| Asian | 12 |
| Native | 12 |
| Hispanic/Latino | 9 |
| Bachelor's or higher | 24 |

## Districts

- [HI-02](/us/states/hi/districts/02.md) — 25% (congressional)
- [HI Senate District 7](/us/states/hi/districts/senate/7.md) — 23% (state senate)
- [HI House District 13](/us/states/hi/districts/house/13.md) — 23% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
