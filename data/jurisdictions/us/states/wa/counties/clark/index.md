---
type: Jurisdiction
title: "Clark County, WA"
classification: county
fips: "53011"
state: "WA"
demographics:
  population: 516959
  population_under_18: 117472
  population_18_64: 313411
  population_65_plus: 86076
  median_household_income: 97536
  poverty_rate: 7.98
  homeownership_rate: 66.35
  unemployment_rate: 5.29
  median_home_value: 522900
  gini_index: 0.4312
  vacancy_rate: 4.09
  race_white: 388754
  race_black: 11253
  race_asian: 26084
  race_native: 3943
  hispanic: 63672
  bachelors_plus: 163945
districts:
  - to: "us/states/wa/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wa/districts/senate/20"
    rel: in-district
    area_weight: 0.5732
  - to: "us/states/wa/districts/senate/17"
    rel: in-district
    area_weight: 0.2155
  - to: "us/states/wa/districts/senate/18"
    rel: in-district
    area_weight: 0.125
  - to: "us/states/wa/districts/senate/49"
    rel: in-district
    area_weight: 0.0862
  - to: "us/states/wa/districts/house/20"
    rel: in-district
    area_weight: 0.5732
  - to: "us/states/wa/districts/house/17"
    rel: in-district
    area_weight: 0.2155
  - to: "us/states/wa/districts/house/18"
    rel: in-district
    area_weight: 0.125
  - to: "us/states/wa/districts/house/49"
    rel: in-district
    area_weight: 0.0862
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Clark County, WA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 516959 |
| Under 18 | 117472 |
| 18–64 | 313411 |
| 65+ | 86076 |
| Median household income | 97536 |
| Poverty rate | 7.98 |
| Homeownership rate | 66.35 |
| Unemployment rate | 5.29 |
| Median home value | 522900 |
| Gini index | 0.4312 |
| Vacancy rate | 4.09 |
| White | 388754 |
| Black | 11253 |
| Asian | 26084 |
| Native | 3943 |
| Hispanic/Latino | 63672 |
| Bachelor's or higher | 163945 |

## Districts

- [WA-03](/us/states/wa/districts/03.md) — 100% (congressional)
- [WA Senate District 20](/us/states/wa/districts/senate/20.md) — 57% (state senate)
- [WA Senate District 17](/us/states/wa/districts/senate/17.md) — 22% (state senate)
- [WA Senate District 18](/us/states/wa/districts/senate/18.md) — 12% (state senate)
- [WA Senate District 49](/us/states/wa/districts/senate/49.md) — 9% (state senate)
- [WA House District 20](/us/states/wa/districts/house/20.md) — 57% (state house)
- [WA House District 17](/us/states/wa/districts/house/17.md) — 22% (state house)
- [WA House District 18](/us/states/wa/districts/house/18.md) — 12% (state house)
- [WA House District 49](/us/states/wa/districts/house/49.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
