---
type: Jurisdiction
title: "Millard County, UT"
classification: county
fips: "49027"
state: "UT"
demographics:
  population: 13315
  population_under_18: 4100
  population_18_64: 6934
  population_65_plus: 2281
  median_household_income: 73639
  poverty_rate: 7.68
  homeownership_rate: 81.75
  unemployment_rate: 5.53
  median_home_value: 284700
  gini_index: 0.3647
  vacancy_rate: 13.64
  race_white: 11250
  race_black: 15
  race_asian: 273
  race_native: 164
  hispanic: 1805
  bachelors_plus: 2318
districts:
  - to: "us/states/ut/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ut/districts/senate/28"
    rel: in-district
    area_weight: 0.8089
  - to: "us/states/ut/districts/senate/27"
    rel: in-district
    area_weight: 0.1911
  - to: "us/states/ut/districts/house/29"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ut]
timestamp: "2026-07-03"
---

# Millard County, UT

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 13315 |
| Under 18 | 4100 |
| 18–64 | 6934 |
| 65+ | 2281 |
| Median household income | 73639 |
| Poverty rate | 7.68 |
| Homeownership rate | 81.75 |
| Unemployment rate | 5.53 |
| Median home value | 284700 |
| Gini index | 0.3647 |
| Vacancy rate | 13.64 |
| White | 11250 |
| Black | 15 |
| Asian | 273 |
| Native | 164 |
| Hispanic/Latino | 1805 |
| Bachelor's or higher | 2318 |

## Districts

- [UT-02](/us/states/ut/districts/02.md) — 100% (congressional)
- [UT Senate District 28](/us/states/ut/districts/senate/28.md) — 81% (state senate)
- [UT Senate District 27](/us/states/ut/districts/senate/27.md) — 19% (state senate)
- [UT House District 29](/us/states/ut/districts/house/29.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
