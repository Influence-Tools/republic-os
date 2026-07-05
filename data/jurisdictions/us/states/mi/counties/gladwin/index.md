---
type: Jurisdiction
title: "Gladwin County, MI"
classification: county
fips: "26051"
state: "MI"
demographics:
  population: 25693
  population_under_18: 4852
  population_18_64: 13822
  population_65_plus: 7019
  median_household_income: 55349
  poverty_rate: 14.88
  homeownership_rate: 86.08
  unemployment_rate: 6.78
  median_home_value: 162300
  gini_index: 0.4337
  vacancy_rate: 33.79
  race_white: 24093
  race_black: 81
  race_asian: 117
  race_native: 126
  hispanic: 575
  bachelors_plus: 4368
districts:
  - to: "us/states/mi/districts/02"
    rel: in-district
    area_weight: 0.9995
  - to: "us/states/mi/districts/senate/34"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mi/districts/house/99"
    rel: in-district
    area_weight: 0.8161
  - to: "us/states/mi/districts/house/95"
    rel: in-district
    area_weight: 0.1838
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Gladwin County, MI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25693 |
| Under 18 | 4852 |
| 18–64 | 13822 |
| 65+ | 7019 |
| Median household income | 55349 |
| Poverty rate | 14.88 |
| Homeownership rate | 86.08 |
| Unemployment rate | 6.78 |
| Median home value | 162300 |
| Gini index | 0.4337 |
| Vacancy rate | 33.79 |
| White | 24093 |
| Black | 81 |
| Asian | 117 |
| Native | 126 |
| Hispanic/Latino | 575 |
| Bachelor's or higher | 4368 |

## Districts

- [MI-02](/us/states/mi/districts/02.md) — 100% (congressional)
- [MI Senate District 34](/us/states/mi/districts/senate/34.md) — 100% (state senate)
- [MI House District 99](/us/states/mi/districts/house/99.md) — 82% (state house)
- [MI House District 95](/us/states/mi/districts/house/95.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
