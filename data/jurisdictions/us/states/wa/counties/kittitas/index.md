---
type: Jurisdiction
title: "Kittitas County, WA"
classification: county
fips: "53037"
state: "WA"
demographics:
  population: 47172
  population_under_18: 7872
  population_18_64: 31260
  population_65_plus: 8040
  median_household_income: 73804
  poverty_rate: 14.38
  homeownership_rate: 61.49
  unemployment_rate: 6.29
  median_home_value: 497400
  gini_index: 0.4743
  vacancy_rate: 18.97
  race_white: 38721
  race_black: 532
  race_asian: 813
  race_native: 237
  hispanic: 4974
  bachelors_plus: 15196
districts:
  - to: "us/states/wa/districts/08"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/wa/districts/senate/13"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/wa/districts/house/13"
    rel: in-district
    area_weight: 0.9994
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Kittitas County, WA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47172 |
| Under 18 | 7872 |
| 18–64 | 31260 |
| 65+ | 8040 |
| Median household income | 73804 |
| Poverty rate | 14.38 |
| Homeownership rate | 61.49 |
| Unemployment rate | 6.29 |
| Median home value | 497400 |
| Gini index | 0.4743 |
| Vacancy rate | 18.97 |
| White | 38721 |
| Black | 532 |
| Asian | 813 |
| Native | 237 |
| Hispanic/Latino | 4974 |
| Bachelor's or higher | 15196 |

## Districts

- [WA-08](/us/states/wa/districts/08.md) — 100% (congressional)
- [WA Senate District 13](/us/states/wa/districts/senate/13.md) — 100% (state senate)
- [WA House District 13](/us/states/wa/districts/house/13.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
