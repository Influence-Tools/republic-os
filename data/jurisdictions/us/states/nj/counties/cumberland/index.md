---
type: Jurisdiction
title: "Cumberland County, NJ"
classification: county
fips: "34011"
state: "NJ"
demographics:
  population: 153305
  population_under_18: 37403
  population_18_64: 91686
  population_65_plus: 24216
  median_household_income: 67436
  poverty_rate: 15.58
  homeownership_rate: 66.53
  unemployment_rate: 6.76
  median_home_value: 221400
  gini_index: 0.4734
  vacancy_rate: 6.11
  race_white: 71835
  race_black: 26429
  race_asian: 2290
  race_native: 2784
  hispanic: 54804
  bachelors_plus: 25817
districts:
  - to: "us/states/nj/districts/02"
    rel: in-district
    area_weight: 0.7439
  - to: "us/states/nj/districts/senate/1"
    rel: in-district
    area_weight: 0.5656
  - to: "us/states/nj/districts/senate/3"
    rel: in-district
    area_weight: 0.1743
  - to: "us/states/nj/districts/house/1"
    rel: in-district
    area_weight: 0.5656
  - to: "us/states/nj/districts/house/3"
    rel: in-district
    area_weight: 0.1743
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nj]
timestamp: "2026-07-03"
---

# Cumberland County, NJ

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 153305 |
| Under 18 | 37403 |
| 18–64 | 91686 |
| 65+ | 24216 |
| Median household income | 67436 |
| Poverty rate | 15.58 |
| Homeownership rate | 66.53 |
| Unemployment rate | 6.76 |
| Median home value | 221400 |
| Gini index | 0.4734 |
| Vacancy rate | 6.11 |
| White | 71835 |
| Black | 26429 |
| Asian | 2290 |
| Native | 2784 |
| Hispanic/Latino | 54804 |
| Bachelor's or higher | 25817 |

## Districts

- [NJ-02](/us/states/nj/districts/02.md) — 74% (congressional)
- [NJ Senate District 1](/us/states/nj/districts/senate/1.md) — 57% (state senate)
- [NJ Senate District 3](/us/states/nj/districts/senate/3.md) — 17% (state senate)
- [NJ House District 1](/us/states/nj/districts/house/1.md) — 57% (state house)
- [NJ House District 3](/us/states/nj/districts/house/3.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
