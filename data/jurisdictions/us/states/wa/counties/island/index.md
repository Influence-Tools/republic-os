---
type: Jurisdiction
title: "Island County, WA"
classification: county
fips: "53029"
state: "WA"
demographics:
  population: 86836
  population_under_18: 15049
  population_18_64: 48528
  population_65_plus: 23259
  median_household_income: 90551
  poverty_rate: 7.7
  homeownership_rate: 74.75
  unemployment_rate: 4.3
  median_home_value: 593300
  gini_index: 0.4197
  vacancy_rate: 15.84
  race_white: 67437
  race_black: 1969
  race_asian: 4291
  race_native: 874
  hispanic: 7582
  bachelors_plus: 32984
districts:
  - to: "us/states/wa/districts/02"
    rel: in-district
    area_weight: 0.4111
  - to: "us/states/wa/districts/senate/10"
    rel: in-district
    area_weight: 0.41
  - to: "us/states/wa/districts/house/10"
    rel: in-district
    area_weight: 0.41
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Island County, WA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 86836 |
| Under 18 | 15049 |
| 18–64 | 48528 |
| 65+ | 23259 |
| Median household income | 90551 |
| Poverty rate | 7.7 |
| Homeownership rate | 74.75 |
| Unemployment rate | 4.3 |
| Median home value | 593300 |
| Gini index | 0.4197 |
| Vacancy rate | 15.84 |
| White | 67437 |
| Black | 1969 |
| Asian | 4291 |
| Native | 874 |
| Hispanic/Latino | 7582 |
| Bachelor's or higher | 32984 |

## Districts

- [WA-02](/us/states/wa/districts/02.md) — 41% (congressional)
- [WA Senate District 10](/us/states/wa/districts/senate/10.md) — 41% (state senate)
- [WA House District 10](/us/states/wa/districts/house/10.md) — 41% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
