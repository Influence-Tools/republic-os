---
type: Jurisdiction
title: "Roane County, WV"
classification: county
fips: "54087"
state: "WV"
demographics:
  population: 13786
  population_under_18: 2763
  population_18_64: 7770
  population_65_plus: 3253
  median_household_income: 45778
  poverty_rate: 19.06
  homeownership_rate: 78.87
  unemployment_rate: 9.11
  median_home_value: 122100
  gini_index: 0.4606
  vacancy_rate: 20.18
  race_white: 13227
  race_black: 3
  race_asian: 34
  race_native: 7
  hispanic: 167
  bachelors_plus: 2103
districts:
  - to: "us/states/wv/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/wv/districts/senate/8"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/wv/districts/house/15"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wv]
timestamp: "2026-07-03"
---

# Roane County, WV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13786 |
| Under 18 | 2763 |
| 18–64 | 7770 |
| 65+ | 3253 |
| Median household income | 45778 |
| Poverty rate | 19.06 |
| Homeownership rate | 78.87 |
| Unemployment rate | 9.11 |
| Median home value | 122100 |
| Gini index | 0.4606 |
| Vacancy rate | 20.18 |
| White | 13227 |
| Black | 3 |
| Asian | 34 |
| Native | 7 |
| Hispanic/Latino | 167 |
| Bachelor's or higher | 2103 |

## Districts

- [WV-01](/us/states/wv/districts/01.md) — 100% (congressional)
- [WV Senate District 8](/us/states/wv/districts/senate/8.md) — 100% (state senate)
- [WV House District 15](/us/states/wv/districts/house/15.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
